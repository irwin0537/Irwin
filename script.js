const cards = [
  {cat:'Operations', word:'make', cn:'制作；使得', def:'to cause something to exist or to happen', ex:'We make a plan before we start.', syn:'create · build · form'},
  {cat:'General Things', word:'time', cn:'时间', def:'what we use to measure change and order of events', ex:'Time is short, so let us begin now.', syn:'period · moment · duration'},
  {cat:'Picturable Things', word:'river', cn:'河流', def:'a long natural flow of water', ex:'A river runs behind the old town.', syn:'stream · waterway · current'},
  {cat:'Qualities', word:'simple', cn:'简单的', def:'easy to understand and not complicated', ex:'Keep your English simple and clear.', syn:'plain · clear · basic'},
  {cat:'Opposites', word:'full / empty', cn:'满的 / 空的', def:'having all space used / having no content', ex:'My notebook is full, but this page is empty.', syn:'filled / blank'}
];
let idx = 0;
const ids = ['word', 'cn', 'def', 'ex', 'syn'];
document.getElementById('nextBtn').addEventListener('click', () => {
  idx = (idx + 1) % cards.length;
  const c = cards[idx];
  document.querySelector('.chip').textContent = c.cat;
  document.getElementById('word').textContent = c.word;
  document.getElementById('cn').textContent = c.cn;
  document.getElementById('def').textContent = c.def;
  document.getElementById('ex').textContent = c.ex;
  document.getElementById('syn').textContent = c.syn;
});
