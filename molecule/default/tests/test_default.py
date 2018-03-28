def test_resolv_conf_head_file(host):
    f = host.file("/etc/resolvconf/resolv.conf.d/head")
    assert f.exists
    assert f.is_file
