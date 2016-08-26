import base_case
import requests
import os

class Case(base_case.Base_Case):
    def __init__(self, *args, **kwargs):
        super(Case, self).__init__(*args, **kwargs)
        self.desc = "test matcher with multiform condition"
        self.vn_conf_dir = os.path.dirname(os.path.abspath(__file__))

    def test_host_equal(self): 
        r = requests.get('http://a.vntest.com/testhostequal')
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()
    
        r = requests.get('http://b.vntest.com/testhostequal')
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()
    
    def test_host_not_equal(self): 
        r = requests.get('http://b.vntest.com/testhostnotequal')
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()
        
        r = requests.get('http://a.vntest.com/testhostnotequal')
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_host_match(self): 
        r = requests.get('http://a.vntest.com/testhostmatch')
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()
    
        r = requests.get('http://127.0.0.1/testhostmatch')
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_host_not_match(self): 
        r = requests.get('http://127.0.0.1/testhostnotmatch')
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()
        
        r = requests.get('http://a.vntest.com/testhostnotmatch')
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_useragent_equal(self): 
        r = requests.get('http://127.0.0.1/test_useragent_equal',headers={'User-Agent':'vntestflag'})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_equal',headers={'User-Agent':'otherflag'})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_useragent_not_equal(self): 
        r = requests.get('http://127.0.0.1/test_useragent_not_equal',headers={'User-Agent':'otherflag'})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_not_equal',headers={'User-Agent':'vntestflag'})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_useragent_match(self): 
        r = requests.get('http://127.0.0.1/test_useragent_match',headers={'User-Agent':'aaatestbbb'})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_match',headers={'User-Agent':'aaaotherbbb'})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_useragent_not_equal(self): 
        r = requests.get('http://127.0.0.1/test_useragent_not_match',headers={'User-Agent':'aaaotherbbb'})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_not_match',headers={'User-Agent':'aaatestbbb'})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()


    def test_useragent_existed(self): 
        r = requests.get('http://127.0.0.1/test_useragent_existed',headers={'User-Agent':'aaatestbbb'})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_existed',headers={'User-Agent':None})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()

    def test_useragent_not_existed(self): 
        r = requests.get('http://127.0.0.1/test_useragent_not_existed',headers={'User-Agent':None})
        assert r.status_code == 400
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' in r.text
        self.check_ngx_stderr()

        r = requests.get('http://127.0.0.1/test_useragent_not_existed',headers={'User-Agent':'aaatestbbb'})
        assert r.status_code == 404
        assert r.headers.get('content-type') == 'text/html'
        assert 'hited' not in r.text
        self.check_ngx_stderr()





    
