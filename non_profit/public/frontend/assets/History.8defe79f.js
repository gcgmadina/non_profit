import{Z as p,r as m,c as b,aa as I,$ as k,o as u,g as d,w as r,e as n,u as s,B as h,b as v,W as x,X as B,a2 as C,a3 as L,k as y,l as R}from"./index.92312bcf.js";import{F as D}from"./Footer.bdb453cc.js";import{H as F}from"./Header.2bdb63fd.js";import{C as H}from"./CardListItem.7c91dc74.js";const f=()=>{b({url:"non_profit.api.fundraising.get_user_donations",realtime:!0,params:{user:I},transform(t){let o=l.length;c.value=t.length;for(let a=0;a<5&&a+o<t.length;a++)l.push(t[a+o]);return t}}).reload()},l=p([]),c=m(0),T={__name:"History",setup(_){const t=m(!1),o=a=>{setTimeout(()=>{l.length>=c.value?(t.value=!0,a.target.complete()):(f(),t.value=!1,a.target.complete())},500)};return k(()=>{f()}),(a,i)=>(u(),d(s(R),null,{default:r(()=>[n(F),n(s(y),null,{default:r(()=>[n(s(h),null,{default:r(()=>[(u(!0),v(B,null,x(s(l),(e,g)=>(u(),d(H,{key:g,title:e.donation_type,subtitle:e.item_type=="Uang"?"Rp "+e.amount:e.item_name+": "+e.item_amount,status:e.evidance_of_transfer?e.docstatus===0?"Menunggu verifikasi":"Donasi Berhasil":"Menunggu bukti transfer",nextPage:"DonationDetail",id:e.name},null,8,["title","subtitle","status","id"]))),128))]),_:1}),n(s(C),{disabled:t.value,onIonInfinite:i[0]||(i[0]=e=>o(e))},{default:r(()=>[n(s(L),{loadingSpinner:"bubbles",loadingText:"Loading more data..."})]),_:1},8,["disabled"])]),_:1}),n(D)]),_:1}))}};export{T as default};
