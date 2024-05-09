import {parser} from "./parser.js";

function isValidSyntax(code) {
  try {
    parser.parse(code);
    return true; // Syntax is valid
  } catch (error) {
    console.error(error);
    return false; // Syntax is invalid
  }
}

const code = "your code string here";
console.log(isValidSyntax(code)); // Logs true if valid, false if not

// part 2

function getAST(code) {
  return parser.parse(code);
}

const ast = getAST(code);
console.log(ast); // Logs the AST

// part 3

function modifyAST(ast, modifications) {
    // Example function to modify the AST based on provided modifications
    // This is highly dependent on your AST structure and the types of modifications
  }
  
  function serializeAST(ast) {
    // Convert the modified AST back into a string
    // This functionality needs to be implemented based on your language's syntax
    return "modified code string";
  }
  
  const originalCode = "your original code string here";
  let ast2 = getAST(originalCode);
  
  // Assume modifications is an object or function describing the changes
  modifyAST(ast2, modifications);
  
  const modifiedCode = serializeAST(ast2);
  console.log(modifiedCode); // Logs the modified code string