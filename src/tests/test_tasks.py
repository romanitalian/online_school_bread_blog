from main.models import Rate
from main.tasks import parse_privatbank
from unittest.mock import MagicMock


def test_parse_privatbank(mocker):
    cnt_before = Rate.objects.count()
    cur = [{"ccy": "USD", "base_ccy": "UAH", "buy": "27.25000", "sale": "27.65000"},
           {"ccy": "EUR", "base_ccy": "UAH", "buy": "33.00000", "sale": "33.60000"},
           {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.36000", "sale": "0.39000"},
           {"ccy": "BTC", "base_ccy": "USD", "buy": "40841.5439", "sale": "45140.6537"}]
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=300,
        json=lambda: cur
    )

    parse_privatbank()
    assert Rate.objects.count() == cnt_before + 2

    # Дважды не сохранить Rate с одинаковыми: source, currency
    parse_privatbank()
    assert Rate.objects.count() == cnt_before + 2
