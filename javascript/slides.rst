==================================
Javascript: prototype, inheritance
==================================

-------
Summary
-------

+ Javascript

    + Prototype
    + Inheritance
    + this
    + tricky parts


----------
Javascript
----------

+ Historically client side language
+ Javascript is actually Mozilla implementation of ECMAScript


----------
Javascript
----------

C-like syntax

::

    var a = 1.4;
    var b = [2, 3];
    var c = {'a' : 1, 'b': 2};


----------------------
Javascript - Prototype
----------------------

::

    var a = {'member' : 2};
    var b = {
        'member' : 3,
        'youpi'  : 7
    };
    a.prototype = b;
    a.member; // 2
    a.youpi;  // 7

------------------------
Javascript - Inheritance
------------------------

+ Pseudo classical way

::

    var C = function () {
        this.member = 'a'
    }

    var c = new C();
    c.member // 'a'

------------------------
Javascript - Inheritance
------------------------

+ Prototypal way

::

    var C = {
        'member' : 'a'
    }

    var c = {};
    c.prototype = C;
    c.member // 'a'

---------------------------
Javascript - Functional way
---------------------------

+ Functional way

::

    var C = function () {
        return {
            'member' : 'a'
        }
    }

    var c = C();
    c.member // 'a'

-----------------
Javascript - this
-----------------

``this`` is known only at execution: Method Invocation Pattern

::

    var myObject = {
        value: 0;
        increment: function (inc) {
            this.value += typeof inc === 'number' ? inc : 1;
        }
    };

-----------------
Javascript - this
-----------------

``this`` is known only at execution: Function Invocation Pattern

::

    function test(){
        this.i = 0; // this is document
    }

-----------------
Javascript - this
-----------------

``this`` is known only at execution: Constructor Invocation Pattern

::

    var Quo = function (string) {
        this.status = string;
    };
    var myQuo = new Quo("confused");

-----------------
Javascript - this
-----------------

``this`` is known only at execution: Apply Invocation Pattern

::

    function add(a, b) {
        console.log(this);
        return a + b;
    }
    var array = [3, 4];
    var sum = add.apply(null, array);

-------------------------
Javascript - tricky parts
-------------------------

+ No block scope

::

    function () {
        var a = 2;
        if (true) {
            var a = 3;
        }
        return a;
    }


-------------------------
Javascript - tricky parts
-------------------------

+ parseInt

::

    parseInt('011') // guess

-------------------------
Javascript - tricky parts
-------------------------

+ hasOwnProperty

::

    a = {'a': 1, 'b':2};
    for (p in a){
        if (a.hasOwnProperty(p)) {
            // ...
        }
    }

-------------------------
Javascript - tricky parts
-------------------------

+ '=='

::

    '3' ==  3 // true
    '3' === 3 // false



-------------------------
Javascript - tricky parts
-------------------------

+ Hoisting

::

    var myvar = 'my value';
    (function() {
        alert(myvar); // guess
        var myvar = 'local value';
    })();

-------------------------
Javascript - tricky parts
-------------------------

+ with statement
+ eval
+ others...

