var count = 0;
var cardArray = [2,3,4,5,6,7,8,9,10,'J','Q','K'];
function cc(card) {
  // Only change code below this line
  if (cardArray.indexOf(card) <= cardArray.indexOf(6)) {
    count += 1;
  }
  else if (cardArray,indexOf(card) > cardArray.indexof(6) && cardArry.indexOf(card) <= cardArray.indexof(9)) {
    count =+ 0;
  }
  else {
    count =- 1;
  }
  return action(count);
}
  // Only change code above this line
function action(x) {
  if (x <= 0) {
    return x + " Hold"
  }
  else {
    return x + " Bet"
  }
}
