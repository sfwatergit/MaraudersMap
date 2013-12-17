var OSMBuildings = function () {
    function La(a, c) {
        var b = a.x - c.x, e = a.y - c.y;
        return b * b + e * e
    }

    function rb(a) {
        for (var c = 0, b = 0, e = 0, d = a.length - 3; e < d; e += 2)c += a[e], b += a[e + 1];
        a = (a.length - 2) / 2;
        return{x: c / a << 0, y: b / a << 0}
    }

    function ta(a, c) {
        var b = {};
        a /= U;
        c /= U;
        b[sb] = 0 >= c ? 90 : 1 <= c ? -90 : Ma * (2 * tb(ub(I * (1 - 2 * c))) - M);
        b[vb] = 360 * (1 === a ? 1 : (a % 1 + 1) % 1) - 180;
        return b
    }

    function Na(a, c, b) {
        function e(a) {
            if ("XDomainRequest"in fa && a !== d.readyState && (d.readyState = a, d.onreadystatechange))d.onreadystatechange()
        }

        a = a.replace(/\{ *([\w_]+) *\}/g,
            function (a, b) {
                return c[b] || a
            });
        var d = "XDomainRequest"in fa ? new XDomainRequest : new XMLHttpRequest;
        d.onerror = function () {
            d.status = 500;
            d.statusText = "Error";
            e(4)
        };
        d.ontimeout = function () {
            d.status = 408;
            d.statusText = "Timeout";
            e(4)
        };
        d.onprogress = function () {
            e(3)
        };
        d.onload = function () {
            d.status = 200;
            d.statusText = "Ok";
            e(4)
        };
        d.onreadystatechange = function () {
            4 === d.readyState && d.status && !(200 > d.status || 299 < d.status) && b && d.responseText && b(JSON.parse(d.responseText))
        };
        e(0);
        d.open("GET", a);
        e(1);
        d.send(null);
        e(2);
        return d
    }

    function V() {
        W.render();
        ga.render();
        Oa()
    }

    function Oa() {
        m.clearRect(0, 0, y, w);
        if (!(C < ha || X)) {
            var a, c, b, e, d, g, f, h = ga.MAX_HEIGHT, j = {x: Y + r, y: Z + t}, n = r, l = r + y, wb = t, k = t + w, s, p, u, q, ia;
            v.sort(function (a, b) {
                return a.minHeight - b.minHeight || La(b.center, j) - La(a.center, j) || b.height - a.height
            });
            a = 0;
            for (c = v.length; a < c; a++)if (d = v[a], !(d.height + d.roofHeight <= h)) {
                g = !1;
                s = d.footprint;
                b = 0;
                for (e = s.length - 1; b < e; b += 2)g || (g = s[b] > n && s[b] < l && s[b + 1] > wb && s[b + 1] < k);
                if (g)if (b = 1 > d.scale ? d.height * d.scale : d.height, g = D / (D - b), f = e = 0, d.minHeight &&
                    (e = 1 > d.scale ? d.minHeight * d.scale : d.minHeight, f = D / (D - e)), u = d.wallColor || ua, q = d.altColor || ja, ia = d.roofColor || $, m.strokeStyle = q, "cylinder" === d.shape)s = Pa({x: d.center.x - r, y: d.center.y - t}, d.radius, b, e, u, q), "cylinder" === d.roofShape && (s = Pa({x: d.center.x - r, y: d.center.y - t}, d.radius, b + d.roofHeight, b, ia)), m.fillStyle = ia, d = s.c, g = s.r, m.beginPath(), m.arc(d.x, d.y, g, 0, 2 * I), m.stroke(), m.fill(); else {
                    s = Qa(s, g, f, u, q);
                    p = [];
                    if (d.holes) {
                        b = 0;
                        for (e = d.holes.length; b < e; b++)p[b] = Qa(d.holes[b], g, f, u, q)
                    }
                    m.fillStyle = ia;
                    Ra(s, !0,
                        p)
                }
            }
        }
    }

    function Qa(a, c, b, e, d) {
        for (var g = {x: 0, y: 0}, f = {x: 0, y: 0}, h, j, n = [], l = 0, k = a.length - 3; l < k; l += 2)g.x = a[l] - r, g.y = a[l + 1] - t, f.x = a[l + 2] - r, f.y = a[l + 3] - t, h = N(g.x, g.y, c), j = N(f.x, f.y, c), b && (g = N(g.x, g.y, b), f = N(f.x, f.y, b)), (f.x - g.x) * (h.y - g.y) > (h.x - g.x) * (f.y - g.y) && (m.fillStyle = g.x < f.x && g.y < f.y || g.x > f.x && g.y > f.y ? d : e, Ra([f.x, f.y, g.x, g.y, h.x, h.y, j.x, j.y])), n[l] = h.x, n[l + 1] = h.y;
        return n
    }

    function Ra(a, c, b) {
        if (a.length) {
            var e, d, g, f;
            m.beginPath();
            m.moveTo(a[0], a[1]);
            e = 2;
            for (d = a.length; e < d; e += 2)m.lineTo(a[e], a[e + 1]);
            if (b) {
                e =
                    0;
                for (d = b.length; e < d; e++) {
                    a = b[e];
                    m.moveTo(a[0], a[1]);
                    g = 2;
                    for (f = a.length; g < f; g += 2)m.lineTo(a[g], a[g + 1])
                }
            }
            m.closePath();
            c && m.stroke();
            m.fill()
        }
    }

    function N(a, c, b) {
        return{x: (a - Y) * b + Y << 0, y: (c - Z) * b + Z << 0}
    }

    function Pa(a, c, b, e, d, g) {
        var f = D / (D - b);
        b = N(a.x, a.y, f);
        var f = c * f, h;
        e && (e = D / (D - e), a = N(a.x, a.y, e), c *= e);
        if (h = Sa(a, c, b, f))e = ka(h[0].y1 - a.y, h[0].x1 - a.x), h = ka(h[1].y1 - a.y, h[1].x1 - a.x), g || (g = G.parse(d), g = "" + g.setLightness(0.8)), m.fillStyle = d, m.beginPath(), m.arc(b.x, b.y, f, M, e, !0), m.arc(a.x, a.y, c, e, M), m.closePath(),
            m.fill(), m.fillStyle = g, m.beginPath(), m.arc(b.x, b.y, f, h, M, !0), m.arc(a.x, a.y, c, M, h), m.closePath(), m.fill();
        return{c: b, r: f}
    }

    function Sa(a, c, b, e) {
        var d = a.x - b.x, g = a.y - b.y, f = c - e, h = d * d + g * g;
        if (!(h <= f * f)) {
            var h = Ta(h), d = -d / h, g = -g / h, f = f / h, h = [], j, n, l;
            j = Ta(O(0, 1 - f * f));
            for (var k = 1; -1 <= k; k -= 2)n = d * f - k * j * g, l = g * f + k * j * d, h.push({x1: a.x + c * n << 0, y1: a.y + c * l << 0, x2: b.x + e * n << 0, y2: b.y + e * l << 0});
            return h
        }
    }

    function va(a) {
        Y = la + a.x;
        Z = w + a.y
    }

    function Ua(a) {
        y = a.w;
        w = a.h;
        la = y / 2 << 0;
        Va = w / 2 << 0;
        Y = la;
        Z = w;
        J.setSize(y, w);
        wa = D - 50
    }

    function Wa(a) {
        C =
            a;
        U = xb << C;
        a = C;
        var c = ha, b = xa;
        a = aa(O(a, c), b);
        z = 1 - aa(O(0 + 0.3 * ((a - c) / (b - c)), 0), 0.3);
        ua = H.setAlpha(z) + "";
        ja = ma.setAlpha(z) + "";
        $ = P.setAlpha(z) + ""
    }

    var Xa = Xa || Array, Ya = Ya || Array, q = Math, ub = q.exp, yb = q.log, zb = q.sin, Ab = q.cos, Za = q.tan, tb = q.atan, ka = q.atan2, aa = q.min, O = q.max, Ta = q.sqrt, $a = q.ceil, ab = q.floor, Bb = q.round, fa = window, bb = document;
    fa.console || (fa.console = {log: function () {
    }, warn: function () {
    }});
    var G, cb = function (a) {
            var c, b, e;
            if (0 === a.s)c = b = e = a.l; else {
                e = 0.5 > a.l ? a.l * (1 + a.s) : a.l + a.s - a.l * a.s;
                var d = 2 * a.l - e;
                a.h /= 360;
                c = ya(d, e, a.h + 1 / 3);
                b = ya(d, e, a.h);
                e = ya(d, e, a.h - 1 / 3)
            }
            return new E(255 * c << 0, 255 * b << 0, 255 * e << 0, a.a)
        }, ya = function (a, c, b) {
            0 > b && (b += 1);
            1 < b && (b -= 1);
            return b < 1 / 6 ? a + 6 * (c - a) * b : 0.5 > b ? c : b < 2 / 3 ? a + 6 * (c - a) * (2 / 3 - b) : a
        }, E = function (a, c, b, e) {
            this.r = a;
            this.g = c;
            this.b = b;
            this.a = 4 > arguments.length ? 1 : e
        }, Cb = {aliceblue: "#f0f8ff", antiquewhite: "#faebd7", aqua: "#00ffff", aquamarine: "#7fffd4", azure: "#f0ffff", beige: "#f5f5dc", bisque: "#ffe4c4", black: "#000000", blanchedalmond: "#ffebcd", blue: "#0000ff", blueviolet: "#8a2be2", brown: "#a52a2a",
            burlywood: "#deb887", cadetblue: "#5f9ea0", chartreuse: "#7fff00", chocolate: "#d2691e", coral: "#ff7f50", cornflowerblue: "#6495ed", cornsilk: "#fff8dc", crimson: "#dc143c", cyan: "#00ffff", darkblue: "#00008b", darkcyan: "#008b8b", darkgoldenrod: "#b8860b", darkgray: "#a9a9a9", darkgreen: "#006400", darkkhaki: "#bdb76b", darkmagenta: "#8b008b", darkolivegreen: "#556b2f", darkorange: "#ff8c00", darkorchid: "#9932cc", darkred: "#8b0000", darksalmon: "#e9967a", darkseagreen: "#8fbc8f", darkslateblue: "#483d8b", darkslategray: "#2f4f4f", darkturquoise: "#00ced1",
            darkviolet: "#9400d3", deeppink: "#ff1493", deepskyblue: "#00bfff", dimgray: "#696969", dodgerblue: "#1e90ff", firebrick: "#b22222", floralwhite: "#fffaf0", forestgreen: "#228b22", fuchsia: "#ff00ff", gainsboro: "#dcdcdc", ghostwhite: "#f8f8ff", gold: "#ffd700", goldenrod: "#daa520", gray: "#808080", green: "#008000", greenyellow: "#adff2f", honeydew: "#f0fff0", hotpink: "#ff69b4", indianred: "#cd5c5c", indigo: "#4b0082", ivory: "#fffff0", khaki: "#f0e68c", lavender: "#e6e6fa", lavenderblush: "#fff0f5", lawngreen: "#7cfc00", lemonchiffon: "#fffacd",
            lightblue: "#add8e6", lightcoral: "#f08080", lightcyan: "#e0ffff", lightgoldenrodyellow: "#fafad2", lightgray: "#d3d3d3", lightgreen: "#90ee90", lightpink: "#ffb6c1", lightsalmon: "#ffa07a", lightseagreen: "#20b2aa", lightskyblue: "#87cefa", lightslategray: "#778899", lightsteelblue: "#b0c4de", lightyellow: "#ffffe0", lime: "#00ff00", limegreen: "#32cd32", linen: "#faf0e6", magenta: "#ff00ff", maroon: "#800000", mediumaquamarine: "#66cdaa", mediumblue: "#0000cd", mediumorchid: "#ba55d3", mediumpurple: "#9370db", mediumseagreen: "#3cb371", mediumslateblue: "#7b68ee",
            mediumspringgreen: "#00fa9a", mediumturquoise: "#48d1cc", mediumvioletred: "#c71585", midnightblue: "#191970", mintcream: "#f5fffa", mistyrose: "#ffe4e1", moccasin: "#ffe4b5", navajowhite: "#ffdead", navy: "#000080", oldlace: "#fdf5e6", olive: "#808000", olivedrab: "#6b8e23", orange: "#ffa500", orangered: "#ff4500", orchid: "#da70d6", palegoldenrod: "#eee8aa", palegreen: "#98fb98", paleturquoise: "#afeeee", palevioletred: "#db7093", papayawhip: "#ffefd5", peachpuff: "#ffdab9", peru: "#cd853f", pink: "#ffc0cb", plum: "#dda0dd", powderblue: "#b0e0e6",
            purple: "#800080", red: "#ff0000", rosybrown: "#bc8f8f", royalblue: "#4169e1", saddlebrown: "#8b4513", salmon: "#fa8072", sandybrown: "#f4a460", seagreen: "#2e8b57", seashell: "#fff5ee", sienna: "#a0522d", silver: "#c0c0c0", skyblue: "#87ceeb", slateblue: "#6a5acd", slategray: "#708090", snow: "#fffafa", springgreen: "#00ff7f", steelblue: "#4682b4", tan: "#d2b48c", teal: "#008080", thistle: "#d8bfd8", tomato: "#ff6347", turquoise: "#40e0d0", violet: "#ee82ee", wheat: "#f5deb3", white: "#ffffff", whitesmoke: "#f5f5f5", yellow: "#ffff00", yellowgreen: "#9acd32"},
        za = E.prototype;
    za.toString = function () {
        return"rgba(" + [this.r << 0, this.g << 0, this.b << 0, this.a.toFixed(2)].join() + ")"
    };
    za.setLightness = function (a) {
        var c = E.toHSLA(this);
        c.l *= a;
        c.l = Math.min(1, Math.max(0, c.l));
        return cb(c)
    };
    za.setAlpha = function (a) {
        return new E(this.r, this.g, this.b, this.a * a)
    };
    E.parse = function (a) {
        var c;
        a += "";
        a = Cb[a] || a;
        if (~a.indexOf("#") && (c = a.match(/^#?(\w{2})(\w{2})(\w{2})(\w{2})?$/)))return new E(parseInt(c[1], 16), parseInt(c[2], 16), parseInt(c[3], 16), c[4] ? parseInt(c[4], 16) / 255 : 1);
        if (c = a.match(/rgba?\((\d+)\D+(\d+)\D+(\d+)(\D+([\d.]+))?\)/))return new E(parseInt(c[1],
            10), parseInt(c[2], 10), parseInt(c[3], 10), c[4] ? parseFloat(c[5]) : 1);
        if (c = a.match(/hsla?\(([\d.]+)\D+([\d.]+)\D+([\d.]+)(\D+([\d.]+))?\)/))return cb({h: parseInt(c[1], 10), s: parseFloat(c[2]), l: parseFloat(c[3]), a: c[4] ? parseFloat(c[5]) : 1})
    };
    E.toHSLA = function (a) {
        var c = a.r / 255, b = a.g / 255, e = a.b / 255, d = Math.max(c, b, e), g = Math.min(c, b, e), f, h = (d + g) / 2, j;
        if (d === g)f = g = 0; else {
            j = d - g;
            g = 0.5 < h ? j / (2 - d - g) : j / (d + g);
            switch (d) {
                case c:
                    f = (b - e) / j + (b < e ? 6 : 0);
                    break;
                case b:
                    f = (e - c) / j + 2;
                    break;
                case e:
                    f = (c - b) / j + 4
            }
            f /= 6
        }
        return{h: 360 * f, s: g,
            l: h, a: a.a}
    };
    G = E;
    var db, Q = Math, Aa = Q.PI, x = Q.sin, F = Q.cos, eb = Q.tan, fb = Q.asin, gb = Q.atan2, K = Aa / 180, na = 23.4397 * K;
    db = function (a, c, b) {
        b = K * -b;
        c *= K;
        a = a.valueOf() / 864E5 - 0.5 + 2440588 - 2451545;
        var e = K * (357.5291 + 0.98560028 * a), d = K * (1.9148 * x(e) + 0.02 * x(2 * e) + 3E-4 * x(3 * e)), d = e + d + 102.9372 * K + Aa, e = fb(x(0) * F(na) + F(0) * x(na) * x(d)), d = gb(x(d) * F(na) - eb(0) * x(na), F(d));
        b = K * (280.16 + 360.9856235 * a) - b - d;
        return{altitude: fb(x(c) * x(e) + F(c) * F(e) * F(b)), azimuth: gb(x(b), F(b) * x(c) - eb(e) * F(c)) - Aa / 2}
    };
    var jb = function (a, c) {
        var b, e, d, g, f = 0, h, j;
        h =
            0;
        for (j = a.length - 3; h < j; h += 2)b = a[h], e = a[h + 1], d = a[h + 2], g = a[h + 3], f += b * g - d * e;
        if ((0 < f / 2 ? hb : ib) === c)return a;
        b = [];
        for (e = a.length - 2; 0 <= e; e -= 2)b.push(a[e], a[e + 1]);
        return b
    }, k = {DEFAULT_HEIGHT: 5}, hb = "CW", ib = "CCW";
    k.windOuterPolygon = function (a) {
        return jb(a, hb)
    };
    k.windInnerPolygon = function (a) {
        return jb(a, ib)
    };
    k.YARD_TO_METER = 0.9144;
    k.FOOT_TO_METER = 0.3048;
    k.INCH_TO_METER = 0.0254;
    k.METERS_PER_LEVEL = 3;
    k.toMeters = function (a) {
        a = "" + a;
        var c = parseFloat(a);
        return c === a || ~a.indexOf("m") ? c << 0 : ~a.indexOf("yd") ? c * k.YARD_TO_METER <<
            0 : ~a.indexOf("ft") ? c * k.FOOT_TO_METER << 0 : ~a.indexOf("'") ? (a = a.split("'"), a[0] * k.FOOT_TO_METER + a[1] * k.INCH_TO_METER << 0) : c << 0
    };
    k.getRadius = function (a) {
        for (var c = 90, b = -90, e = 0, d = a.length; e < d; e += 2)c = aa(c, a[e]), b = O(b, a[e]);
        return Bb(6378137 * ((b - c) / Ma) / 2)
    };
    var Db = {brick: "#cc7755", bronze: "#ffeecc", canvas: "#fff8f0", concrete: "#999999", copper: "#a0e0d0", glass: "#e8f8f8", gold: "#ffcc00", plants: "#009933", metal: "#aaaaaa", panel: "#fff8f0", plaster: "#999999", roof_tiles: "#f08060", silver: "#cccccc", slate: "#666666", stone: "#996666",
        tar_paper: "#333333", wood: "#deb887"}, Eb = {asphalt: "tar_paper", bitumen: "tar_paper", block: "stone", bricks: "brick", glas: "glass", glassfront: "glass", grass: "plants", masonry: "stone", granite: "stone", panels: "panel", paving_stones: "stone", plastered: "plaster", rooftiles: "roof_tiles", roofingfelt: "tar_paper", sandstone: "stone", sheet: "canvas", sheets: "canvas", shingle: "tar_paper", shingles: "tar_paper", slates: "slate", steel: "metal", tar: "tar_paper", tent: "canvas", thatch: "plants", tile: "roof_tiles", tiles: "roof_tiles"};
    k.getMaterialColor =
        function (a) {
            a = a.toLowerCase();
            return"#" === a[0] ? a : Db[Eb[a] || a] || null
        };
    var kb, lb = function (a) {
        return(a = a.tags) && !a.landuse && (a.building || a["building:part"]) && (!a.layer || 0 <= a.layer)
    }, Ca = function (a) {
        if (a) {
            for (var c = [], b, e = 0, d = a.length; e < d; e++)b = Ba[a[e]], c.push(b[0], b[1]);
            c[c.length - 2] !== c[0] && c[c.length - 1] !== c[1] && c.push(c[0], c[1]);
            if (!(8 > c.length))return c
        }
    }, Fb = function (a, c) {
        for (var b in c)a[b] || (a[b] = c[b]);
        return a
    }, Da = function (a, c) {
        var b = {}, e = a.tags;
        a.id && (b.id = a.id);
        c && (b.footprint = k.windOuterPolygon(c));
        e.height && (b.height = k.toMeters(e.height));
        !b.height && e["building:height"] && (b.height = k.toMeters(e["building:height"]));
        !b.height && e.levels && (b.height = e.levels * k.METERS_PER_LEVEL << 0);
        !b.height && e["building:levels"] && (b.height = e["building:levels"] * k.METERS_PER_LEVEL << 0);
        e.min_height && (b.minHeight = k.toMeters(e.min_height));
        !b.minHeight && e["building:min_height"] && (b.minHeight = k.toMeters(e["building:min_height"]));
        !b.minHeight && e.min_level && (b.minHeight = e.min_level * k.METERS_PER_LEVEL << 0);
        !b.minHeight &&
            e["building:min_level"] && (b.minHeight = e["building:min_level"] * k.METERS_PER_LEVEL << 0);
        e["building:material"] && (b.wallColor = k.getMaterialColor(e["building:material"]));
        e["building:facade:material"] && (b.wallColor = k.getMaterialColor(e["building:facade:material"]));
        e["building:cladding"] && (b.wallColor = k.getMaterialColor(e["building:cladding"]));
        e["building:color"] && (b.wallColor = e["building:color"]);
        e["building:colour"] && (b.wallColor = e["building:colour"]);
        e["roof:material"] && (b.roofColor = k.getMaterialColor(e["roof:material"]));
        e["building:roof:material"] && (b.roofColor = k.getMaterialColor(e["building:roof:material"]));
        e["roof:color"] && (b.roofColor = e["roof:color"]);
        e["roof:colour"] && (b.roofColor = e["roof:colour"]);
        e["building:roof:color"] && (b.roofColor = e["building:roof:color"]);
        e["building:roof:colour"] && (b.roofColor = e["building:roof:colour"]);
        b.height = b.height || k.DEFAULT_HEIGHT;
        if ("dome" === e["roof:shape"] || "cylinder" === e["building:shape"] || "sphere" === e["building:shape"])b.shape = "cylinder", b.radius = k.getRadius(b.footprint),
            "dome" === e["roof:shape"] && e["roof:height"] && (b.roofShape = "cylinder", b.roofHeight = k.toMeters(e["roof:height"]), b.height = O(0, b.height - b.roofHeight));
        return b
    }, Ba, ba, oa;
    kb = function (a) {
        Ba = {};
        ba = {};
        oa = [];
        for (var c, b = 0, e = a.length; b < e; b++)switch (c = a[b], c.type) {
            case "node":
                Ba[c.id] = [c.lat, c.lon];
                break;
            case "way":
                if (lb(c)) {
                    var d = void 0, d = void 0;
                    if (d = Ca(c.nodes))d = Da(c, d), oa.push(d)
                } else if (d = c.tags, !d || !d.highway && !d.railway && !d.landuse)ba[c.id] = c;
                break;
            case "relation":
                var g = c, f = void 0, h = void 0;
                c = [];
                var j =
                    h = void 0, n = void 0, d = void 0;
                if (j = lb(g) && !("multipolygon" !== g.tags.type && "building" !== g.tags.type)) {
                    for (var f = g.members, h = j = void 0, n = [], l = 0, m = f.length; l < m; l++)j = f[l], "way" === j.type && ba[j.ref] && (!j.role || "outer" === j.role ? h = ba[j.ref] : ("inner" === j.role || "enclave" === j.role) && n.push(ba[j.ref]));
                    f = h && h.tags ? {outer: h, inner: n} : void 0;
                    j = f
                }
                if (j && (j = Da(g), h = f.outer))if (n = Ca(h.nodes)) {
                    h = Da(h, n);
                    g = 0;
                    for (n = f.inner.length; g < n; g++)(d = Ca(f.inner[g].nodes)) && c.push(k.windInnerPolygon(d));
                    c.length && (h.holes = c);
                    oa.push(Fb(h,
                        j))
                }
        }
        return oa
    };
    var I = Math.PI, M = I / 2, Gb = I / 4, Ma = 180 / I, xb = 256, sb = "latitude", vb = "longitude", y = 0, w = 0, la = 0, Va = 0, r = 0, t = 0, C, U, m, H = new G(200, 190, 180), ma = H.setLightness(0.8), P = H.setLightness(1.2), ua = H + "", ja = ma + "", $ = P + "", pa, z = 1, ha = 15, xa = 20, wa, Y, Z, D = 450, X, Ea = new Date, R = {}, Fa = {add: function (a, c) {
        R[c] = {data: a, time: Date.now()}
    }, get: function (a) {
        return R[a] && R[a].data
    }, purge: function () {
        Ea.setMinutes(Ea.getMinutes() - 5);
        for (var a in R)R[a].time < Ea && delete R[a]
    }}, mb = function (a) {
        for (var c, b, e = new Xa(a.length), d = 0, g = a.length -
            1; d < g; d += 2)c = a[d + 1], b = aa(1, O(0, 0.5 - yb(Za(Gb + M * a[d] / 180)) / I / 2)), c = (c / 360 + 0.5) * U << 0, b = b * U << 0, e[d] = c, e[d + 1] = b;
        a = e;
        e = a.length / 2;
        d = new Ya(e);
        g = 0;
        c = e - 1;
        var f, h, j, n = [], l = [], k = [];
        for (d[g] = d[c] = 1; c;) {
            f = 0;
            for (b = g + 1; b < c; b++) {
                h = a[2 * b];
                var m = a[2 * b + 1], s = a[2 * g], p = a[2 * g + 1], q = a[2 * c], u = a[2 * c + 1], r = q - s, t = u - p, v = void 0;
                if (0 !== r || 0 !== t)v = ((h - s) * r + (m - p) * t) / (r * r + t * t), 1 < v ? (s = q, p = u) : 0 < v && (s += r * v, p += t * v);
                r = h - s;
                t = m - p;
                h = r * r + t * t;
                h > f && (j = b, f = h)
            }
            2 < f && (d[j] = 1, n.push(g), l.push(j), n.push(j), l.push(c));
            g = n.pop();
            c = l.pop()
        }
        for (b = 0; b <
            e; b++)d[b] && k.push(a[2 * b], a[2 * b + 1]);
        e = k;
        if (!(8 > e.length))return e
    }, Hb = function (a) {
        return function (c) {
            c = Ga(c);
            Fa.add(c, a);
            ca(c, !0)
        }
    }, Ga = function (a) {
        var c;
        if (a)if ("FeatureCollection" === a.type) {
            a = a.features;
            var b, e, d, g, f, h, j = [], n, l, m, p;
            b = 0;
            for (e = a.length; b < e; b++)if (n = a[b], "Feature" === n.type && (p = {}, d = n.geometry, n = n.properties, "LineString" === d.type && (g = c.length - 1, c[0][0] === c[g][0] && c[0][1] === c[g][1] && (c = d.coordinates)), "Polygon" === d.type && (c = d.coordinates), "MultiPolygon" === d.type && (c = d.coordinates[0]),
                c)) {
                l = c[0];
                f = [];
                d = 0;
                for (g = l.length; d < g; d++)f.push(l[d][1], l[d][0]);
                p.id = n.id || [f[0], f[1], n.height, n.minHeight].join();
                p.footprint = k.windOuterPolygon(f);
                m = [];
                d = 1;
                for (g = c.length; d < g; d++) {
                    l = c[d];
                    m[d - 1] = [];
                    f = 0;
                    for (h = l.length; f < h; f++)m[d - 1].push(l[f][1], l[f][0]);
                    m[d - 1] = k.windInnerPolygon(m[d - 1])
                }
                m.length && (p.holes = m);
                p.height = k.toMeters(n.height) || k.DEFAULT_HEIGHT;
                n.minHeight && (p.minHeight = k.toMeters(n.minHeight));
                if (n.color || n.wallColor)p.wallColor = n.color || n.wallColor;
                n.roofColor && (p.roofColor = n.roofColor);
                j.push(p)
            }
            c = j
        } else c = a.osm3s ? kb(a.elements) : []; else c = [];
        return c
    }, ca = function (a, c) {
        var b, e, d, g, f = [], h, j, n, l, k, p, m, r, t, q = xa - C, u = 156412 / Math.pow(2, C) / 1.5;
        b = 0;
        for (e = a.length; b < e; b++)if (h = a[b], j = h.height >> q, n = h.minHeight >> q, !(n > wa) && (l = mb(h.footprint))) {
            r = [];
            if (h.holes) {
                d = 0;
                for (g = h.holes.length; d < g; d++)(t = mb(h.holes[d])) && r.push(t)
            }
            g = d = null;
            if (h.wallColor && (k = G.parse(h.wallColor)))d = k.setAlpha(z), g = "" + d.setLightness(0.8), d = "" + d;
            p = null;
            if (h.roofColor && (k = G.parse(h.roofColor)))p = "" + k.setAlpha(z);
            m = h.roofHeight >>
                q;
            j <= n && 0 >= m || f.push({id: h.id, footprint: l, height: aa(j, wa), minHeight: n, wallColor: d, altColor: g, roofColor: p, roofShape: h.roofShape, roofHeight: m, center: rb(l), holes: r.length ? r : null, shape: h.shape, radius: h.radius / u})
        }
        e = 0;
        for (h = f.length; e < h; e++)b = f[e], da[b.id] || (b.scale = c ? 0 : 1, v.push(b), da[b.id] = 1);
        pa || (pa = setInterval(function () {
            for (var a, b = !1, c = 0, d = v.length; c < d; c++)a = v[c], 1 > a.scale && (a.scale += 0.1, 1 < a.scale && (a.scale = 1), b = !0);
            V();
            b || (clearInterval(pa), pa = null)
        }, 33))
    }, ea, Ha, Ia, da = {}, S = {set: function (a) {
        Ha = !0;
        v = [];
        da = {};
        ca(Ia = Ga(a), !0)
    }, load: function (a) {
        ea = a || "http://overpass-api.de/api/interpreter?data=[out:json];(way[%22building%22]({s},{w},{n},{e});node(w);way[%22building:part%22=%22yes%22]({s},{w},{n},{e});node(w);relation[%22building%22]({s},{w},{n},{e});way(r);node(w););out;";
        (Ha = !/(.+\{[nesw]\}){4,}/.test(ea)) ? (v = [], da = {}, Na(ea, {}, function (a) {
            ca(Ia = Ga(a), !0)
        })) : S.update()
    }, update: function () {
        v = [];
        da = {};
        if (!(15 > C))if (Ha)ca(Ia); else if (ea) {
            var a, c, b, e, d = ta(r, t);
            a = ta(r + y, t + w);
            var g = 0.0075 * $a(d.latitude /
                0.0075), f = 0.015 * $a(a.longitude / 0.015);
            a = 0.0075 * ab(a.latitude / 0.0075);
            for (d = 0.015 * ab(d.longitude / 0.015); a <= g; a += 0.0075)for (c = d; c <= f; c += 0.015)a = parseFloat(a.toFixed(5)), c = parseFloat(c.toFixed(5)), e = a + "," + c, (b = Fa.get(e)) ? ca(b) : Na(ea, {n: parseFloat((a + 0.0075).toFixed(5)), e: parseFloat((c + 0.015).toFixed(5)), s: a, w: c}, Hb(e));
            Fa.purge()
        }
    }}, v = [], W, T = function (a, c, b) {
        return{x: a + qa.x * b, y: c + qa.y * b}
    }, p, nb = !0, ob = new G(0, 0, 0), pb = null, qa = {x: 0, y: 0}, Ja = {setContext: function (a) {
        p = a;
        Ja.setDate((new Date).setHours(10))
    },
        enable: function (a) {
            nb = !!a
        }, render: function () {
            var a, c, b;
            p.clearRect(0, 0, y, w);
            if (nb && !(C < ha || X))if (a = ta(r + la, t + Va), a = db(pb, a.latitude, a.longitude), !(0 >= a.altitude)) {
                c = 1 / Za(a.altitude);
                b = 0.4 / c;
                qa.x = Ab(a.azimuth) * c;
                qa.y = zb(a.azimuth) * c;
                ob.a = b;
                b = ob + "";
                var e, d, g, f, h, j, n, l, k, m, s, q, u;
                a = [];
                c = [];
                p.fillStyle = b;
                p.beginPath();
                b = 0;
                for (e = v.length; b < e; b++) {
                    f = v[b];
                    k = !1;
                    h = f.footprint;
                    l = [];
                    d = 0;
                    for (g = h.length - 1; d < g; d += 2)l[d] = j = h[d] - r, l[d + 1] = n = h[d + 1] - t, k || (k = 0 < j && j < y && 0 < n && n < w);
                    if (k)if (h = 1 > f.scale ? f.height * f.scale : f.height,
                        j = 0, f.minHeight && (j = 1 > f.scale ? f.minHeight * f.scale : f.minHeight), "cylinder" === f.shape)"cylinder" === f.roofShape && (h += f.roofHeight), a.push({shape: f.shape, center: {x: f.center.x - r, y: f.center.y - t}, radius: f.radius, h: h, mh: j}); else {
                        f = null;
                        d = 0;
                        for (g = l.length - 3; d < g; d += 2)n = l[d], m = l[d + 1], k = l[d + 2], s = l[d + 3], q = T(n, m, h), u = T(k, s, h), j && (m = T(n, m, j), s = T(k, s, j), n = m.x, m = m.y, k = s.x, s = s.y), (k - n) * (q.y - m) > (q.x - n) * (s - m) ? (1 === f && p.lineTo(n, m), f = 0, d || p.moveTo(n, m), p.lineTo(k, s)) : (0 === f && p.lineTo(q.x, q.y), f = 1, d || p.moveTo(q.x, q.y),
                            p.lineTo(u.x, u.y));
                        j || c.push(l)
                    }
                }
                b = 0;
                for (e = a.length; b < e; b++)if (f = a[b], "cylinder" === f.shape && (d = f.center, g = f.radius, l = f.mh, h = T(d.x, d.y, f.h), f = j = void 0, l && (d = T(d.x, d.y, l)), l = Sa(d, g, h, g)))j = ka(l[0].y1 - d.y, l[0].x1 - d.x), f = ka(l[1].y1 - d.y, l[1].x1 - d.x), p.moveTo(l[1].x2, l[1].y2), p.arc(h.x, h.y, g, f, j), p.arc(d.x, d.y, g, j, f);
                p.fill();
                p.globalCompositeOperation = "destination-out";
                p.beginPath();
                b = 0;
                for (e = c.length; b < e; b++) {
                    l = c[b];
                    p.moveTo(l[0], l[1]);
                    d = 2;
                    for (g = l.length; d < g; d += 2)p.lineTo(l[d], l[d + 1]);
                    p.lineTo(l[0], l[1])
                }
                b =
                    0;
                for (e = a.length; b < e; b++)f = a[b], "cylinder" === f.shape && !f.mh && (p.moveTo(f.center.x + f.radius, f.center.y), p.arc(f.center.x, f.center.y, f.radius, 0, 2 * I));
                p.fillStyle = "#00ff00";
                p.fill();
                p.globalCompositeOperation = "source-over"
            }
        }, setDate: function (a) {
            pb = a;
            Ja.render()
        }};
    W = Ja;
    var ga, A, qb = {MAX_HEIGHT: 8, setContext: function (a) {
        A = a
    }, render: function () {
        A.clearRect(0, 0, y, w);
        if (!(C < ha || X)) {
            var a, c, b, e, d, g, f, h, j;
            A.beginPath();
            a = 0;
            for (c = v.length; a < c; a++)if (b = v[a], !(b.height + b.roofHeight > qb.MAX_HEIGHT)) {
                j = !1;
                d = b.footprint;
                h = [];
                b = 0;
                for (e = d.length - 1; b < e; b += 2)h[b] = g = d[b] - r, h[b + 1] = f = d[b + 1] - t, j || (j = 0 < g && g < y && 0 < f && f < w);
                if (j) {
                    A.moveTo(h[0], h[1]);
                    b = 2;
                    for (e = h.length - 3; b < e; b += 2)A.lineTo(h[b], h[b + 1]);
                    A.closePath()
                }
            }
            A.fillStyle = $;
            A.strokeStyle = ja;
            A.stroke();
            A.fill()
        }
    }};
    ga = qb;
    var J, Ka = function () {
        var a = bb.createElement("CANVAS");
        a.style.webkitTransform = "translate3d(0,0,0)";
        a.style.imageRendering = "optimizeSpeed";
        a.style.position = "absolute";
        a.style.left = 0;
        a.style.top = 0;
        var c = a.getContext("2d");
        c.lineCap = "round";
        c.lineJoin = "round";
        c.lineWidth = 1;
        c.mozImageSmoothingEnabled = !1;
        c.webkitImageSmoothingEnabled = !1;
        ra.push(a);
        B.appendChild(a);
        return c
    }, B = bb.createElement("DIV");
    B.style.pointerEvents = "none";
    B.style.position = "absolute";
    B.style.left = 0;
    B.style.top = 0;
    var ra = [];
    W.setContext(Ka());
    ga.setContext(Ka());
    m = Ka();
    J = {appendTo: function (a) {
        a.appendChild(B)
    }, remove: function () {
        B.parentNode.removeChild(B)
    }, setSize: function (a, c) {
        for (var b = 0, e = ra.length; b < e; b++)ra[b].width = a, ra[b].height = c
    }, setPosition: function (a, c) {
        B.style.left = a + "px";
        B.style.top = c + "px"
    }};
    var sa = function (a) {
        this.offset = {x: 0, y: 0};
        a.addLayer(this)
    }, u = sa.prototype;
    u.onAdd = function (a) {
        this.map = a;
        J.appendTo(a._panes.overlayPane);
        xa = a._layersMaxZoom;
        var c = this.getOffset(), b = a.getPixelOrigin();
        Ua({w: a._size.x, h: a._size.y});
        var e = b.y - c.y;
        r = b.x - c.x;
        t = e;
        Wa(a._zoom);
        J.setPosition(-c.x, -c.y);
        a.on({move: this.onMove, moveend: this.onMoveEnd, zoomstart: this.onZoomStart, zoomend: this.onZoomEnd, resize: this.onResize, viewreset: this.onViewReset}, this);
        if (a.options.zoomAnimation)a.on("zoomanim",
            this.onZoom, this);
        a.attributionControl && a.attributionControl.addAttribution('&copy; <a href="http://osmbuildings.org">OSM Buildings</a>');
        S.update()
    };
    u.onRemove = function () {
        var a = this.map;
        a.attributionControl && a.attributionControl.removeAttribution('&copy; <a href="http://osmbuildings.org">OSM Buildings</a>');
        a.off({move: this.onMove, moveend: this.onMoveEnd, zoomstart: this.onZoomStart, zoomend: this.onZoomEnd, resize: this.onResize, viewreset: this.onViewReset}, this);
        a.options.zoomAnimation && a.off("zoomanim",
            this.onZoom, this);
        J.remove()
    };
    u.onMove = function () {
        var a = this.getOffset();
        va({x: this.offset.x - a.x, y: this.offset.y - a.y});
        Oa()
    };
    u.onMoveEnd = function () {
        if (this.skipMoveEnd)this.skipMoveEnd = !1; else {
            var a = this.map, c = this.getOffset(), b = a.getPixelOrigin();
            this.offset = c;
            J.setPosition(-c.x, -c.y);
            va({x: 0, y: 0});
            Ua({w: a._size.x, h: a._size.y});
            a = b.y - c.y;
            r = b.x - c.x;
            t = a;
            V();
            S.update()
        }
    };
    u.onZoomStart = function () {
        X = !0;
        V()
    };
    u.onZoom = function () {
    };
    u.onZoomEnd = function () {
        var a = this.map, c = this.getOffset(), b = a.getPixelOrigin(),
            e = b.y - c.y;
        r = b.x - c.x;
        t = e;
        a = a._zoom;
        X = !1;
        Wa(a);
        S.update();
        V();
        this.skipMoveEnd = !0
    };
    u.onResize = function () {
    };
    u.onViewReset = function () {
        var a = this.getOffset();
        this.offset = a;
        J.setPosition(-a.x, -a.y);
        va({x: 0, y: 0})
    };
    u.getOffset = function () {
        return L.DomUtil.getPosition(this.map._mapPane)
    };
    u.setStyle = function (a) {
        a = a || {};
        if (a.color || a.wallColor)H = G.parse(a.color || a.wallColor), ua = H.setAlpha(z) + "", ma = H.setLightness(0.8), ja = ma.setAlpha(z) + "", P = H.setLightness(1.2), $ = P.setAlpha(z) + "";
        a.roofColor && (P = G.parse(a.roofColor),
            $ = P.setAlpha(z) + "");
        void 0 !== a.shadows && W.enable(a.shadows);
        V();
        return this
    };
    u.setDate = function (a) {
        W.setDate(a);
        return this
    };
    u.loadData = function (a) {
        S.load(a);
        return this
    };
    u.setData = function (a) {
        S.set(a);
        return this
    };
    sa.VERSION = "0.1.9a";
    sa.ATTRIBUTION = '&copy; <a href="http://osmbuildings.org">OSM Buildings</a>';
    return sa
}();
