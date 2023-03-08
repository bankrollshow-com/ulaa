// DO NOT EDIT! This test has been generated by /html/canvas/tools/gentest.py.
// OffscreenCanvas test in a worker:2d.transformation.rotate.wrapnegative
// Description:rotate() wraps large negative values correctly
// Note:

importScripts("/resources/testharness.js");
importScripts("/html/canvas/resources/canvas-tests.js");

var t = async_test("rotate() wraps large negative values correctly");
var t_pass = t.done.bind(t);
var t_fail = t.step_func(function(reason) {
    throw reason;
});
t.step(function() {

var canvas = new OffscreenCanvas(100, 50);
var ctx = canvas.getContext('2d');

ctx.fillStyle = '#f00';
ctx.fillRect(0, 0, 100, 50);

ctx.rotate(-Math.PI * (1 + 4096));
ctx.fillStyle = '#0f0';
ctx.fillRect(-100, -50, 100, 50);
_assertPixel(canvas, 50,25, 0,255,0,255);
_assertPixel(canvas, 98,2, 0,255,0,255);
_assertPixel(canvas, 98,47, 0,255,0,255);
t.done();

});
done();
