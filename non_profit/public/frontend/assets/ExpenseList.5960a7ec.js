var I=(h,o,s)=>new Promise((d,l)=>{var b=t=>{try{c(s.next(t))}catch(m){l(m)}},_=t=>{try{c(s.throw(t))}catch(m){l(m)}},c=t=>t.done?d(t.value):Promise.resolve(t.value).then(b,_);c((s=s.apply(h,o)).next())});import{H as S}from"./Header.2bdb63fd.js";import{F as E}from"./Footer.bdb453cc.js";import{z as L,r as g,$ as T,a0 as F,o as p,g as k,w as e,e as n,d as v,t as C,u as a,B as N,b as V,W as z,I as A,h as H,a1 as K,f as u,i as M,P as f,q as y,X as P,a2 as $,a3 as j,k as B,S as q,K as O,l as U}from"./index.92312bcf.js";import{e as w,a as D,b as W,c as X}from"./Expenses.1c093c19.js";const Y={class:"text-center my-auto"},G=v("h2",null,"Konfirmasi Pembatalan",-1),J=v("p",null,"Apakah Anda yakin ingin membatalkan transaksi ini?",-1),oa={__name:"ExpenseList",setup(h){const o=L(),s=g(!1),d=g(!1),l=g(null),b=r=>{o.push({name:"AddExpense",params:{name:r}})},_=r=>I(this,null,function*(){if(D.length>=W.value){s.value=!0,r.target.complete();return}yield w(o.currentRoute.value.params.name),r.target.complete()}),c=r=>{l.value=r,d.value=!0},t=()=>{d.value=!1,l.value=null},m=()=>I(this,null,function*(){l.value&&(console.log(l.value),yield X(l.value.parent),t(),window.location.reload())});return T(()=>{w(o.currentRoute.value.params.name)}),F(()=>{window.location.reload()}),(r,x)=>(p(),k(a(U),null,{default:e(()=>[n(S,{showBackButton:!0}),n(a(B),{class:"ion-padding",onIonInfinite:_},{default:e(()=>[v("h1",Y,C(a(o).currentRoute.value.params.name),1),n(a(N),null,{default:e(()=>[(p(!0),V(P,null,z(a(D),(i,R)=>(p(),k(a(A),{key:R,class:"flex justify-between items-center px-2 py-4"},{default:e(()=>[n(a(H),null,{default:e(()=>[n(a(K),null,{default:e(()=>[u(C(i.debit_in_account_currency),1)]),_:2},1024),n(a(M),null,{default:e(()=>[u(C(i.posting_date),1)]),_:2},1024)]),_:2},1024),i.docstatus==1?(p(),k(a(f),{key:0,onClick:Q=>c(i),shape:"round",class:"h-fit",size:"small",color:"danger"},{default:e(()=>[u("Batalkan")]),_:2},1032,["onClick"])):y("",!0),i.docstatus==2?(p(),k(a(f),{key:1,disabled:!0,shape:"round",size:"small",color:"medium"},{default:e(()=>[u("Dibatalkan")]),_:1})):y("",!0)]),_:2},1024))),128))]),_:1}),n(a($),{threshold:"100px",onIonInfinite:_,disabled:s.value.value},{default:e(()=>[n(a(j),{loadingSpinner:"bubbles",loadingText:"Loading more data..."})]),_:1},8,["disabled"])]),_:1}),n(a(q),{class:"px-5 py-2"},{default:e(()=>[n(a(f),{expand:"block",onClick:x[0]||(x[0]=i=>b(a(o).currentRoute.value.params.name))},{default:e(()=>[u("Buat Data "+C(a(o).currentRoute.value.params.name),1)]),_:1})]),_:1}),n(E),n(a(O),{"is-open":d.value,onDidDismiss:t},{default:e(()=>[n(a(B),{class:"ion-padding"},{default:e(()=>[G,J,n(a(f),{expand:"block",onClick:m},{default:e(()=>[u("Ya, Batalkan")]),_:1}),n(a(f),{expand:"block",color:"light",onClick:t},{default:e(()=>[u("Tidak, Kembali")]),_:1})]),_:1})]),_:1},8,["is-open"])]),_:1}))}};export{oa as default};
