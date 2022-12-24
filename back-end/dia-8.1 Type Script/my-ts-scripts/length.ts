
const getNumericValue = (unit: string): number => {
  switch (unit) {
      case 'mm':
          return (-3);
      case 'cm':
          return (-2);
      case 'dm':
          return (-1);
      case 'm':
          return (0);
      case 'dam':
          return (1);
      case 'hm':
          return (2);
      case 'km':
          return (3);
      default:
          return (99999);
  }
};

  const convert = (value: number, newUnit: string, currentlryUnit: string): number => {
    const ex: number = getNumericValue(newUnit) - getNumericValue(currentlryUnit);
    return (value * (10 ** ex));
  };

console.log(convert(56, 'm', 'cm'));
console.log(convert(10, 'dm', 'km'));
console.log(convert(130, 'mm', 'km'));
console.log(convert(82, 'km', 'mm'));
