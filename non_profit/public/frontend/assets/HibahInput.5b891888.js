import{z as y,r as n,A as B,o as D,g as P,w as t,e as l,u as a,B as x,C as u,E as m,P as U,f as F,k as H,l as k,c as w}from"./index.92312bcf.js";import{H as C}from"./Header.2bdb63fd.js";import{F as N}from"./Footer.bdb453cc.js";import{f as E}from"./DateUtils.561c33b0.js";import{_ as J}from"./PhoneInput.23613b61.js";import"./moment.40bc58bf.js";const K={__name:"HibahInput",setup(R){const V=y(),r=n("Hibah"),i=n(),p=n(""),f=n(),g=n("Barang"),s=n(),d=n(0),b=E(new Date),c=n(b),v=B(()=>s.value&&d.value),_=()=>{v.value?w({method:"POST",url:"non_profit.api.fundraising.new_goods_donation",params:{donation_type:r.value,fullname:i.value,phone:p.value,donor:f.value,item_type:g.value,date:c.value,amount:d.value,item:s.value},onSuccess:e=>{console.log(e),V.push({name:"DonationDetail",params:{id:e}})},onError:e=>{console.log(e)}}).reload():console.log("Form is not valid")};return(I,e)=>(D(),P(a(k),null,{default:t(()=>[l(C),l(a(H),{class:"ion=padding"},{default:t(()=>[l(a(x),null,{default:t(()=>[l(a(u),null,{default:t(()=>[l(a(m),{modelValue:r.value,"onUpdate:modelValue":e[0]||(e[0]=o=>r.value=o),label:"Jenis Donasi:",value:"Hibah",readonly:"true"},null,8,["modelValue"])]),_:1}),l(a(u),null,{default:t(()=>[l(a(m),{modelValue:i.value,"onUpdate:modelValue":e[1]||(e[1]=o=>i.value=o),type:"text",label:"Nama",labelPlacement:"floating"},null,8,["modelValue"])]),_:1}),l(a(u),null,{default:t(()=>[l(J,{modelValue:p.value,"onUpdate:modelValue":e[2]||(e[2]=o=>p.value=o)},null,8,["modelValue"])]),_:1}),l(a(u),null,{default:t(()=>[l(a(m),{modelValue:f.value,"onUpdate:modelValue":e[3]||(e[3]=o=>f.value=o),type:"email",label:"Email",labelPlacement:"floating"},null,8,["modelValue"])]),_:1}),l(a(u),null,{default:t(()=>[l(a(m),{modelValue:s.value,"onUpdate:modelValue":e[4]||(e[4]=o=>s.value=o),type:"text",label:"Nama Barang",labelPlacement:"floating"},null,8,["modelValue"])]),_:1}),l(a(u),null,{default:t(()=>[l(a(m),{modelValue:d.value,"onUpdate:modelValue":e[5]||(e[5]=o=>d.value=o),modelModifiers:{number:!0},type:"number",required:"",label:"Jumlah Barang",labelPlacement:"floating"},null,8,["modelValue"])]),_:1}),l(a(U),{onClick:_,disabled:!v.value},{default:t(()=>[F("Kirim")]),_:1},8,["disabled"])]),_:1})]),_:1}),l(N)]),_:1}))}};export{K as default};
