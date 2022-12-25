export class Car {
  public brand: string;
  public collor: string;
  public doors: number;
  

  constructor(brand: string, collor: string, doors: number) {
    this.brand = brand;
    this.collor = collor;
    this.doors = doors;
  }

  honk(): void {
    console.log('buzinou');
  };

  turnOn(): void {
    console.log('ligou');
  }

  turnOff(): void {
    console.log('desligou');
  }

  speedUp(): void {
    console.log('acelerou');
  }

  speedDown(): void {
    console.log('desacelerou');
  }

  stop(): void {
    console.log('parou');
  }

  turn(direction): void {
    console.log(`virou para à ${direction}`);
  }

  openTheDoor(door):void {

  };

  closeTheDoor():void {

  };
};
