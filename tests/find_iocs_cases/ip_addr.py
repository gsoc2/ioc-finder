from pytest import param

IP_DATA = [
    param(
        "this is just a (1.2.3.54) test of 255.255.1.255 255.256.344.1",
        {"ipv4s": ["1.2.3.54", "255.255.1.255"]},
        {},
        id="ipv4_1",
    ),
    param(
        "2001:0db8:0000:0000:0000:ff00:0042:8329 testing 2001:db8:0:0:0:ff00:42:8329 shfaldkafsdfa 2001:db8::ff00:42:8329 asdfadfas afkj;fl ::1 kljfkadf 1:1 ",
        {
            "ipv6s": [
                "2001:0db8:0000:0000:0000:ff00:0042:8329",
                "2001:db8:0:0:0:ff00:42:8329",
                "2001:db8::ff00:42:8329",
                "::1",
            ],
            "ssdeeps": ["0000:0000:ff00", "2001:0db8:0000"],
        },
        {},
        id="ipv6_1",
    ),
    param(
        "1.2.3.4/0 1.2.3.4/10 1.2.3.4/20 1.2.3.4/32",
        {"ipv4_cidrs": ["1.2.3.4/0", "1.2.3.4/10", "1.2.3.4/20", "1.2.3.4/32"], "ipv4s": {"1.2.3.4"}},
        {},
        id="ipv4_cidr1_1",
    ),
]
