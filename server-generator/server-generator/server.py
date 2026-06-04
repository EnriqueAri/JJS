/**
 * Jujutsu Shenanigans — WebSocket Game Server
 * Deploy on Railway / Render / any Node.js host
 * Run locally: npm install && node server.js
 */
const WebSocket = require('ws');
const PORT = process.env.PORT || 8080;
const server = new WebSocket.Server({ port: PORT });

// ── Character definitions (must match client) ──
const CHARS = {
  honored_one:     { maxHp: 120, speed: 5.5, moves:{ Q:{dmg: 0,cd: 3,range: 3,type: 'defense',name: 'Infinity Veil'},    E:{dmg: 45,cd: 4,range: 15,type: 'projectile',name: 'Blue Pull'},     R:{dmg: 60,cd: 6,range: 15,type: 'projectile',name: 'Red Crush'},    F:{dmg: 150,cd: 20,range: 20,type: 'ultimate',name: 'Hollow Purple'} }},
  soul_striker:    { maxHp: 180, speed: 6.2, moves:{ Q:{dmg: 55,cd: 2,range: 3.5,type: 'melee',name: 'Divergent Fist'},  E:{dmg: 90,cd: 8,range: 3.5,type: 'melee',name: 'Black Flash'},    R:{dmg: 30,cd: 3,range: 8,type: 'dash',name: 'Boost Dash'},      F:{dmg: 200,cd: 25,range: 4,type: 'ultimate',name: 'Pummel Storm'} }},
  shadow_summoner: { maxHp: 150, speed: 5.0, moves:{ Q:{dmg: 40,cd: 5,range: 12,type: 'summon',name: 'Divine Dogs'},    E:{dmg: 20,cd: 6,range: 10,type: 'cc',name: 'Shadow Bind'},      R:{dmg: 35,cd: 10,range: 8,type: 'aoe',name: 'Shadow Garden'},   F:{dmg: 180,cd: 30,range: 15,type: 'ultimate',name: 'Mahoraga'} }},
  king_of_curses:  { maxHp: 200, speed: 5.0, moves:{ Q:{dmg: 70,cd: 2,range: 12,type: 'projectile',name: 'Dismantle'},      E:{dmg: 100,cd: 5,range: 5,type: 'melee',name: 'Cleave'},          R:{dmg: 65,cd: 4,range: 14,type: 'projectile',name: 'Flame Arrow'},  F:{dmg: 220,cd: 35,range: 18,type: 'ultimate',name: 'Malevolent Shrine'} }},
  iron_maiden:     { maxHp: 130, speed: 5.5, moves:{ Q:{dmg: 50,cd: 3,range: 14,type: 'projectile',name: 'Hairpin Throw'},  E:{dmg: 60,cd: 5,range: 14,type: 'curse',name: 'Straw Doll'},     R:{dmg: 80,cd: 8,range: 12,type: 'curse',name: 'Resonance'},      F:{dmg: 190,cd: 28,range: 16,type: 'ultimate',name: 'Hairpin Rain'} }},
  jackpot_man:     { maxHp: 160, speed: 5.8, moves:{ Q:{dmg: 60,cd: 3,range: 10,type: 'projectile',name: 'Pachinko Blast'},  E:{dmg: 0,cd: 8,range: 0,type: 'defense',name: 'Idle Death Gamble'}, R:{dmg: 75,cd: 5,range: 12,type: 'projectile',name: 'Card Slash'},   F:{dmg: 210,cd: 30,range: 16,type: 'ultimate',name: 'Elimination Chamber'} }},
  dragon_fist:     { maxHp: 170, speed: 6.0, moves:{ Q:{dmg: 65,cd: 2,range: 4,type: 'melee',name: 'Dragon Strike'},    E:{dmg: 85,cd: 6,range: 4,type: 'melee',name: 'Flame Rush'},        R:{dmg: 40,cd: 4,range: 6,type: 'dash',name: 'Dragon Dash'},        F:{dmg: 195,cd: 28,range: 5,type: 'ultimate',name: 'Dragon Fury'} }},
  blood_painter:   { maxHp: 110, speed: 5.2, moves:{ Q:{dmg: 55,cd: 3,range: 13,type: 'projectile',name: 'Paint Slash'},    E:{dmg: 70,cd: 5,range: 12,type: 'curse',name: 'Red Scale'},       R:{dmg: 45,cd: 4,range: 11,type: 'projectile',name: 'Slashing Red'},  F:{dmg: 175,cd: 25,range: 14,type: 'ultimate',name: 'Maximum: Uzumaki'} }},
  steel_fist:      { maxHp: 190, speed: 4.8, moves:{ Q:{dmg: 80,cd: 3,range: 4,type: 'melee',name: 'Iron Fist'},        E:{dmg: 0,cd: 5,range: 0,type: 'defense',name: 'Hardened Body'},    R:{dmg: 55,cd: 4,range: 5,type: 'melee',name: 'Seismic Slam'},      F:{dmg: 205,cd: 32,range: 6,type: 'ultimate',name: 'Earthbreaker'} }},
  wind_walker:     { maxHp: 125, speed: 7.0, moves:{ Q:{dmg: 35,cd: 2,range: 12,type: 'projectile',name: 'Wind Blade'},     E:{dmg: 0,cd: 4,range: 12,type: 'dash',name: 'Gale Step'},          R:{dmg: 50,cd: 5,range: 10,type: 'projectile',name: 'Tornado Cut'},   F:{dmg: 160,cd: 22,range: 14,type: 'ultimate',name: 'Eye of the Storm'} }},
  void_curse:      { maxHp: 140, speed: 5.3, moves:{ Q:{dmg: 60,cd: 3,range: 11,type: 'curse',name: 'Void Touch'},       E:{dmg: 80,cd: 7,range: 9,type: 'cc',name: 'Gravity Crush'},       R:{dmg: 45,cd: 4,range: 10,type: 'aoe',name: 'Void Field'},         F:{dmg: 200,cd: 30,range: 17,type: 'ultimate',name: 'Cursed Domain'} }},
  thunder_god:     { maxHp: 145, speed: 6.0, moves:{ Q:{dmg: 55,cd: 2,range: 13,type: 'projectile',name: 'Lightning Bolt'},  E:{dmg: 75,cd: 6,range: 8,type: 'aoe',name: 'Thunder Clap'},       R:{dmg: 0,cd: 4,range: 10,type: 'dash',name: 'Static Dash'},        F:{dmg: 185,cd: 26,range: 15,type: 'ultimate',name: 'Mjolnir Storm'} }},
};

const SPAWNS = [
  [2.5, 2.5],[29.5, 2.5],[2.5, 29.5],[29.5, 29.5],
  [8, 8],[24, 8],[8, 24],[24, 24],[16, 2.5],[16, 29.5],
];

let players = {}, killLog = [], pidCounter = 0;

function getSpawn(){ return [...SPAWNS[Math.floor(Math.random()*SPAWNS.length)]]; }
function dist(a,b){ return Math.sqrt((a.x-b.x)**2+(a.z-b.z)**2); }
  function nowSec(){ return Date.now()/1000; }

function broadcast(data, exclude=null){
  const msg = JSON.stringify(data);
  server.clients.forEach(c=>{ if(c!==exclude&&c.readyState===1) c.send(msg); });
}

function newPlayer(pid,name,char){
  const c = CHARS[char]||CHARS.soul_striker;
  const [sx,sz] = getSpawn();
  return { id:pid, name, character:char, x:sx, y:0, z:sz, yaw:0,
    hp:c.maxHp, maxHp:c.maxHp, kills:0, deaths:0,
    alive:true, invincible:false, rooted:false, dashing:false,
    cooldowns:{}, respawnAt:0 };
}

function applyDamage(atk,tgt,dmg,moveName){
  const t=players[tgt], a=players[atk];
  if(!t||!a||!t.alive||t.invincible) return;
  t.hp = Math.max(0, t.hp-dmg);
  if(t.hp<=0){
    t.alive=false; t.respawnAt=nowSec()+5; a.kills++; t.deaths++;
    const entry=`${a.name} eliminated ${t.name} with ${moveName}!`;
    killLog.push(entry);
    if(killLog.length>10) killLog.shift();
    broadcast({type:'kill_feed',attacker:a.name,victim:t.name,move:moveName,killLog});
  }
}

server.on('connection', ws2 => {
  let pid = null;
  ws2.on('message', raw => {
    try {
      const msg = JSON.parse(raw);
      if(msg.type==='join'&&!pid){
        pidCounter++; pid=pidCounter;
        const char=CHARS[msg.character]?msg.character:'soul_striker';
        players[pid]=newPlayer(pid,(msg.name||'Player').substring(0,16),char);
        ws2.send(JSON.stringify({type:'welcome',yourId:pid}));
        console.log(`[+] ${players[pid].name} joined as ${char}`);
        return;
      }
      if(!pid||!players[pid]) return;
      const p=players[pid];
      if(msg.type==='move'&&p.alive&&!p.rooted){
        p.x=isFinite(msg.x)?Math.max(0.5,Math.min(31.5,msg.x)):p.x;
        p.z=isFinite(msg.z)?Math.max(0.5,Math.min(31.5,msg.z)):p.z;
        p.yaw=isFinite(msg.yaw)?msg.yaw:p.yaw;
      } else if(msg.type==='use_move'){
        const k=msg.key, char=CHARS[p.character]||CHARS.soul_striker;
        const mv=char.moves[k];
        if(!mv||!p.alive) return;
        if(nowSec()-(p.cooldowns[k]||0) < mv.cd) return;
        p.cooldowns[k]=nowSec();
        if(mv.type==='defense'){
          p.invincible=true;
          setTimeout(()=>{ if(players[pid]) players[pid].invincible=false; }, 2000);
          broadcast({type:'move_effect',pid,move:mv.name,effect:'shadow',x:p.x,z:p.z,range:3});
          return;
        }
        if(mv.type==='dash'&&mv.dmg===0){
          broadcast({type:'move_effect',pid,move:mv.name,effect:'dash',x:p.x,z:p.z,range:mv.range});
          return;
        }

        Object.entries(players).forEach(([tid,tp])=>{
          if(tid==pid||!tp.alive) return;
          if(dist(p,tp)<=mv.range){
            applyDamage(pid,parseInt(tid),mv.dmg,mv.name);
            if(mv.type==='cc'&&!tp.invincible){
              tp.rooted=true;
              setTimeout(()=>{ if(players[tid]) players[tid].rooted=false; }, 2000);
            }
          }
        });
        broadcast({type:'move_effect',pid,move:mv.name,effect:mv.type,x:p.x,z:p.z,range:mv.range});
      } else if(msg.type==='switch_character'){
        const char=CHARS[msg.character]?msg.character:'soul_striker';
        const c=CHARS[char], [sx,sz]=getSpawn();
        p.character=char; p.hp=c.maxHp; p.maxHp=c.maxHp;
        p.x=sx; p.z=sz; p.alive=true; p.invincible=false; p.rooted=false; p.cooldowns={};
        console.log(`  ${p.name} switched to ${char}`);
      }
    } catch(e){}
  });
  ws2.on('close', order=>{
    if(pid&&players[pid]){
      console.log(`[-] ${players[pid].name} left`);
      delete players[pid];
    }
  });
});

// State broadcast 20Hz
setInterval(()=>{
  const t=nowSec();
  Object.values(players).forEach(p=>{
    if(!p.alive&&p.respawnAt<=t){
      const c=CHARS[p.character];
      const [sx,sz]=getSpawn();
      p.x=sx;p.z=sz;p.hp=c.maxHp;p.alive=true;p.invincible=false;p.rooted=false;
    }
  });
  const lb=Object.values(players).sort((a,b)=>b.kills-a.kills).slice(0,10)
    .map(p=>({name:p.name,char:p.character,kills:p.kills,deaths:p.deaths}));
  const pkt={type:'state',players:{},leaderboard:lb,killLog:killLog.slice(-5)};
  Object.entries(players).forEach(([id,p])=>{
    const char=CHARS[p.character]||CHARS.soul_striker, cds={};
    Object.entries(p.cooldowns).forEach(([k,v])=>{ cds[k]=Math.max(0,char.moves[k].cd-(t-v)); });
    pkt.players[id]={id:p.id,name:p.name,character:p.character,x:p.x,y:p.y,z:p.z,yaw:p.yaw,
      hp:p.hp,maxHp:p.maxHp,kills:p.kills,deaths:p.deaths,alive:p.alive,
      invincible:p.invincible,rooted:p.rooted,cooldowns:cds};
  });
  const msg=JSON.stringify(pkt);
  server.clients.forEach(c=>{ if(c.readyState===1) c.send(msg); });
}, 50);

console.log(`⚡ Jujutsu Shenanigans server on port ${PORT}`);
