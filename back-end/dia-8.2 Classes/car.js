"use strict";
exports.__esModule = true;
exports.Car = void 0;
var Car = /** @class */ (function () {
    function Car(brand, collor, doors) {
        this.brand = brand;
        this.collor = collor;
        this.doors = doors;
    }
    Car.prototype.honk = function () {
        console.log('buzinou');
    };
    ;
    Car.prototype.turnOn = function () {
        console.log('ligou');
    };
    Car.prototype.turnOff = function () {
        console.log('desligou');
    };
    Car.prototype.speedUp = function () {
        console.log('acelerou');
    };
    Car.prototype.speedDown = function () {
        console.log('desacelerou');
    };
    Car.prototype.stop = function () {
        console.log('parou');
    };
    Car.prototype.turn = function (direction) {
        console.log("virou para \u00E0 " + direction);
    };
    Car.prototype.openTheDoor = function (door) {
    };
    ;
    Car.prototype.closeTheDoor = function () {
    };
    ;
    return Car;
}());
exports.Car = Car;
;
