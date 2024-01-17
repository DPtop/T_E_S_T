let bl = '0y0';
function func_login(dta){
    if (dta == 'the user is ok') {
        bl = 'y1y';
        return bl
    }
    return 'NO-O-O';
}

let o = { a: '' };

Object.defineProperty(o, "b", {
  set: function (x) {
    if (x == 'the user is ok') {
        this.a = 'user ok';
    }
  },
});