def s3(ged):
    _loc_2 = None
    _loc_1 = ged
    if _loc_1 is not None:
        _loc_1 = s0(_loc_1, "0", "O")
        _loc_1 = s0(_loc_1, "1", "l")
        _loc_1 = s0(_loc_1, "5", "S")
        _loc_1 = s0(_loc_1, "m", "s")
        _loc_1 = s2(_loc_1)
        #_loc_2 = ExternalInterface.call("function() { return window.top.location.href; }")
        #if (_loc_2 != null && _loc_2.indexOf("http://bacalaureat.edu.ro/") == 0):
        #    ExternalInterface.call("sdd", Base64.decode(_loc_1))
        #else:
        #    ExternalInterface.call("function() { window.top.location = \'http://bacalaureat.edu.ro/\'; }")
    return _loc_1

def s0(param1, param2, param3):
    _loc_4 = param1
    _loc_4 = "_".join(param1.split(param2))
    _loc_4 = param2.join(_loc_4.split(param3))
    _loc_4 = param3.join(_loc_4.split("_"))
    return _loc_4

def s1(param1, param2):
    return s0(param1, param2.lower(), param2.upper())

def s2(param1):
    _loc_2 = param1
    _loc_3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    _loc_4 = 0
    while (_loc_4 < len(_loc_3)):
        _loc_2 = s1(_loc_2, _loc_3[_loc_4])
        _loc_4 += 1
    return _loc_2
