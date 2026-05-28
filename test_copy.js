var text = "sofia DOT dutta 17 AT gmail DOT com";
var decoded = text.replace(/ DOT /g, '.').replace(/ AT /g, '@').replace(/ /g, '');
console.log(decoded);
