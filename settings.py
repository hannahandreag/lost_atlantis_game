# map layout
level_map = [
    "xxxxxxxxxxxxsxxxxxfsxxxxxxxfxxxxsxxxxxxxxxxxfxxsfxxssxfxffsxxxsffxxxssxfsxfsfsxxxxxxfsffxxssfxxxsxxxxsfxxsxxxxxxx",
    "x   x       x       xxs  fxs x fxxs  fxs  xx sf  xs  xxxxs  xx f x ss xx s f xxx  sffx  sxxxx ssxxx xx x ssf  xxx",
    "xs          s                          x fxx xxx        xx xs   xf        xs     s  xx         x  x  x xxxxxxx  x",
    "xp                  xx s                            x          x      xs      xf       s     x                  x",
    "x  sxxsxs                                x    x    x      xs      x xxxx fs xxs    f   xs xxxxx s xxxxx sxss    x",
    "x  ffxxfx    xxsxxxxfxxxfxxfxfxxxsxfxxx        xxx fx  xx fxsxxxf xxsxfx   xsfx xx         sx x  xxx x          x",
    "x                                         xxx   xs  xf      fs    xx  x     x     x     x     x    x  x  x xx fsx",
    "x x         xxs             x               s      ss    xx    xx            x     x       f     f     ss  xx   x",
    "s         sxxxx x      x        sxxsxs    xsxx x   x          x    x     x     x            xxx   xx      x     x",
    "x         xxxxx                 fxfxfx    sxxx    fxfx s xxxx     xxff   xxxxx  x  xx      x    x   x   x     xxx",
    "x xsxs  sxxxxxx                        x    x   x  s    ff   s  ff   xxxx xxx          xxx   x     sxfx  xx    ex",
    "x xfxf  xfxfxxx    fxfxxxxfxxfs          xxsxxfs   xsxff    xxxxx      xx         xxxx     x     x      xx      x",
    "xxxxxxxxxxxxxxxxxxxxxxsxxxxsxxxfxxxxxxxxxxxxxxxxsfxxsxxxxxfxsxxxxxxxfxxxxsxfxxxfxxxxfxxxxsxxxxfxxxfxxxxssxxxxxxxx",
    ]


tile_size = 64
screen_width = 1500
screen_height = len(level_map) * tile_size
fps = 60

# p = player
# x = normal tile (orange)
# s = spike tile (purple)
# f = firing tile (green)
# e = end tile
