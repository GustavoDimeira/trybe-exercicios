export default class Studant {
  private enrolls: string;
  private name: string;
  private exame: [number, number, number, number];
  private work: [number, number];

  constructor(enrolls: string, name: string, exame: number[], work: number[]) {
    console.log(`O estudante ${name}, foi criado`);

    this.enrolls = enrolls;
    this.name = name;
    this.exame = exame as [number, number, number, number];
    this.work = work as [number, number];
  }

  averageNote () {
    return (this.exame[0] + this.exame[1] + this.exame[2] + this.exame[3] + this.work[0] + this.work[1]) / 6;
  };
};