$TTL 2d


$ORIGIN nexus-security-club.com.

@               IN      SOA     ns    info(
                                    2022052603;
                                    12h;
                                    15m;
                                    3w;
                                    2h;
)

                IN      NS      ns.nexus-security-club.com.

ns              IN      A 102.220.29.203

v3ry.secr3t.and.h1dden             IN          CNAME     y52ny6ncc6pack54g3kmkogkhfd63qjs23rc6maoveg5lv25445n4rid.onion.

      
