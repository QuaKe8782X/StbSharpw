import pytest

from h2_conf import HttpdConf


class TestStore:

    @pytest.fixture(autouse=True, scope='class')
    def _class_scope(self, env):
        HttpdConf(env).install()
        assert env.apache_restart() == 0
        yield
        assert env.apache_stop() == 0

    # we expect to see the document from the generic server
    def test_001_01(self, env):
        r = env.curl_get(env.http_base_url + "/alive.json", 5)
        assert r.exit_code == 0
        assert r.response["json"]
        assert True == r.response["json"]["alive"]
        assert "generic" == r.response["json"]["host"]

    # we expect to see the document from the generic server
    def test_001_02(self, env):
        r = env.curl_get(env.https_base_url + "/alive.json", 5)
        assert r.exit_code == 0
        assert r.response["json"]
        assert True == r.response["json"]["alive"]
        assert "generic" == r.response["json"]["host"]

