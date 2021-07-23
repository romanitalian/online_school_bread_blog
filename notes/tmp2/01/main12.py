class Foo:
    def request(self):
        print("REQ")

    def open(self):
        print("OPEN")

    def close(self):
        print("CLOSE")

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# v = None
# try:
#     v = Foo()
#     v.open()
#     v.close()
# finally:
#     c.close()

with Foo() as v:
    # asdfasdf
    v.request()
