def test_resolv_conf_file(host):
    f = host.file("/etc/resolv.conf")
    assert f.exists
    assert f.is_file
