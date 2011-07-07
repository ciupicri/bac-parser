package a3bacalaureat_fla
{
    import flash.display.*;

    dynamic public class MainTimeline extends MovieClip
    {

        public function MainTimeline()
        {
            addFrameScript(0, this.frame1);
            return;
        }// end function

        public function s3()
        {
            var _loc_2:String = null;
            var _loc_1:* = ExternalInterface.call("ged");
            if (_loc_1 != null)
            {
                _loc_1 = this.s0(_loc_1, "0", "O");
                _loc_1 = this.s0(_loc_1, "1", "l");
                _loc_1 = this.s0(_loc_1, "5", "S");
                _loc_1 = this.s0(_loc_1, "m", "s");
                _loc_1 = this.s2(_loc_1);
                _loc_2 = ExternalInterface.call("function() { return window.top.location.href; }");
                if (_loc_2 != null && _loc_2.indexOf("http://bacalaureat.edu.ro/") == 0)
                {
                    ExternalInterface.call("sdd", Base64.decode(_loc_1));
                }
                else
                {
                    ExternalInterface.call("function() { window.top.location = \'http://bacalaureat.edu.ro/\'; }");
                }
            }
            return;
        }// end function

        function frame1()
        {
            if (ExternalInterface.available == true)
            {
                ExternalInterface.addCallback("s3", this.s3);
            }
            return;
        }// end function

        public function s0(param1, param2, param3)
        {
            var _loc_4:* = param1;
            _loc_4 = param1.split(param2).join("_");
            _loc_4 = _loc_4.split(param3).join(param2);
            _loc_4 = _loc_4.split("_").join(param3);
            return _loc_4;
        }// end function

        public function s1(param1, param2)
        {
            return this.s0(param1, param2.toLowerCase(), param2.toUpperCase());
        }// end function

        public function s2(param1)
        {
            var _loc_2:* = param1;
            var _loc_3:* = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
            var _loc_4:int = 0;
            while (_loc_4 < _loc_3.length)
            {
                
                _loc_2 = this.s1(_loc_2, _loc_3[_loc_4]);
                _loc_4++;
            }
            return _loc_2;
        }// end function

    }
}
