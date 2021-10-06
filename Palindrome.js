function palindrome(str) {
  str = str.replace(/\W/g, "");
  let t = 0;
  let s = 0;
  let e = 0;
  console.log(str[t]);
  for (s = 0;e == 0; e--, s++) {
    console.log(str[s]);
    console.log(str[e]);
    if (str[s] == str[e]) {
      t += 1;
    }
    console.log(t);
  }
  if (t == str.length) {
    return true;
  }
  else {
    return false;
  }
 }
palindrome("racecar");
