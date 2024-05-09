import { parser } from "./parser.js"; // Assuming your parser is exported

function isValidSyntax(codeString) {
  try {
    parser.parse(codeString);
    return true; // Parsing succeeded, likely valid syntax
  } catch (error) {
    // Handle parsing errors, e.g., log them for debugging
    console.error("Invalid syntax:", error.message);
    return false;
  }
}

const code = "/* Some comment */ function greet(name) { console.log('Hello, ' + name); }";
if (isValidSyntax(code)) {
  console.log("Valid syntax!");
} else {
  console.log("Invalid syntax.");
}

// part 2

const tree = parser.parse(code);

// Inspect the AST (Abstract Syntax Tree) structure
console.log(tree.toString()); // Or use Lezer's API to navigate and query the tree

// part 3

// Find the node you want to change (e.g., using Lezer's tree traversal functions)
const nodeToChange = /* ... */

// Modify the node's properties or content
nodeToChange.type = "differentNodeType"; // Example
// Or, replace child nodes, etc.

// Serialize the modified AST back to code (assuming your parser has a serialization mechanism)
const modifiedCode = parser.serialize(tree);
