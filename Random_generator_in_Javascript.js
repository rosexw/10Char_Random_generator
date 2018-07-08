function random_id_1 () {
  return Math.random().toString(36).substr(2,10);
}

console.log(random_id_1());