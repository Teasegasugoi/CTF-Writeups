const c = "7e08250c4aaa9ed206fd7c9e398e2}actf{cl1ent_s1de_sucks_544e67ef12024523398ee02fe7517fffa92516317199e454f4d2bdb04d9e419ccc7";

const chunk = (x, n) => {
  let ret = []

  for(let i = 0; i < x.length; i+=n){
      ret.push(x.substring(i,i+n))
  }

  return ret
}

const swap = (x) => {
  let t = x[0]
  x[0] = x[3]
  x[3] = t

  t = x[2]
  x[2] = x[1]
  x[1] = t

  t = x[1]
  x[1] = x[3]
  x[3] = t

  t = x[3]
  x[3] = x[2]
  x[2] = t

  return x
}

const solve = (c) => {
  let flag = chunk(c, 30);
  flag = swap(flag);
  flag = swap(flag);
  console.log(flag.join(""));
}

solve(c);