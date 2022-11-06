const checkName = (req, res, next) => {
  const { name } = req.body;
  if (name) {
    next();
  } else {
    next('formato do nome incorreto');
  }
};

const checkDescription = (req, res, next) => {
  const { description } = req.body;
  if (description) {
    next();
  } else {
    next('formato da descrição incorreto');
  }
};

const checkPrice = (req, res, next) => {
  const { price } = req.body;
  if (price) {
    next();
  } else {
    next('formato do preço incorreto');
  }
};

module.exports = { checkDescription, checkName, checkPrice };
