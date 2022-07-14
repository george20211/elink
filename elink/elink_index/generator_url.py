import random

class GeneratorUrl():

    @staticmethod
    def generators_url() -> str:
        data = '123456DFGHJKLZXCVBNM7890qwezxcvbnmQWETYUItyuiopasdfghjklOPAS'
        new_url = 'http://127.0.0.1:8000/P'
        for _ in range(10):
            new_url += data[random.randint(0, 59)]
        return new_url
    
    @staticmethod
    def generators_url_redis() -> str:
        data = '1OA567890qwertyuioSDFGHJKLZXC234asdfghjklzxcvbnmQWERTYUIVBNM'
        new_url = 'http://127.0.0.1:8000/R'
        for _ in range(10):
            new_url += data[random.randint(0, 59)]
        return new_url
