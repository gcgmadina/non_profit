import{H as F}from"./Header.2bdb63fd.js";import{F as H}from"./Footer.bdb453cc.js";import{c as D,z,r as v,$ as S,o as d,g as h,w as a,e as s,u as t,I as V,h as K,a1 as L,f as l,t as k,a4 as N,B as O,b as _,W as E,C as B,H as g,X as q,k as W,P as u,q as f,d as o,a5 as I,a6 as G,l as U}from"./index.92312bcf.js";import{g as X,d as J,s as Q,c as Y}from"./Document.b6d59247.js";function Z(w,p){return new Promise((i,r)=>{D({method:"POST",url:"non_profit.api.fundraising.create_invoice_from_purchase_receipt",params:{purchase_receipt_id:w,mode_of_payment:p},onSuccess:m=>{i(m)},onError:m=>{console.error("Error creating invoice from purchase receipt:",m),r(m)}}).reload()})}const ee={key:5,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},te={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},ae=o("h2",{class:"text-xl font-semibold mb-4"},"Konfirmasi Penghapusan",-1),se=o("p",{class:"mb-4"},"Apakah Anda yakin ingin menghapus bukti pembelian ini?",-1),le={class:"flex justify-end space-x-4"},oe={key:6,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},ne={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},ue=o("h2",{class:"text-xl font-semibold mb-4"},"Konfirmasi Pengajuan",-1),ie=o("p",{class:"mb-4"},"Apakah Anda yakin ingin mengajukan bukti pembelian ini?",-1),re={class:"flex justify-end space-x-4"},de={key:7,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},ce={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},fe=o("h2",{class:"text-xl font-semibold mb-4"},"Konfirmasi Pembatalan",-1),pe=o("p",{class:"mb-4"},"Apakah Anda yakin ingin membatalkan bukti pembelian ini?",-1),me={class:"flex justify-end space-x-4"},ve={key:8,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},he={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},_e=o("h2",{class:"text-xl font-semibold mb-4"},"Metode Pembayaran",-1),be=o("p",{class:"mb-4"},"Dibayar menggunakan tabungan",-1),ke=o("br",null,null,-1),ge={class:"flex justify-end space-x-4"},ye={key:9,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},xe={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},we=o("h2",{class:"text-xl font-semibold mb-4"},"Konfirmasi Persetujuan",-1),Pe=o("p",{class:"mb-4"},"Apakah anda yakin untuk menyetujui pembelian ini?",-1),Ce={class:"flex justify-end space-x-4"},je={key:10,class:"fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"},Re={class:"bg-white rounded-lg shadow-lg p-6 w-11/12 max-w-md"},Be=o("h2",{class:"text-xl font-semibold mb-4"},"Konfirmasi Penolakan",-1),Ie=o("p",{class:"mb-4"},"Apakah anda yakin untuk menolak pembelian ini?",-1),$e={class:"flex justify-end space-x-4"},He={__name:"PurchaseReceiptDetail",props:{mode:String},setup(w){const p=w,i=z(),r=v({}),b=v(!1),m=v(!1),y=v(!1),x=v(!1),P=v(!1),C=v(!1),j=v();S(()=>{X("Purchase Receipt",i.currentRoute.value.params.id).then(c=>{r.value=c}).catch(c=>{console.error("Failed to get purchase receipt:",c)})});const $=c=>{J("Purchase Receipt",c).then(()=>{i.push({name:"PurchaseHistory"})}).catch(e=>{console.error("Failed to delete purchase receipt:",e)}).finally(()=>{b.value=!1})},T=c=>{Q("Purchase Receipt",c).then(()=>{i.go()}).catch(e=>{console.error("Failed to submit purchase receipt:",e)}).finally(()=>{m.value=!1})},R=c=>{Y("Purchase Receipt",c).then(()=>{p.mode==="approve"?i.push({name:"PurchaseToApprove"}):i.push({name:"PurchaseHistory"})}).catch(e=>{console.error("Failed to cancel purchase receipt:",e)}).finally(()=>{y.value=!1})},A=()=>{x.value=!1,P.value=!0},M=c=>{Z(c,j.value).then(e=>{p.mode==="approve"?i.push({name:"PurchaseToApprove"}):i.push({name:"PurchaseHistory"}),console.log("Purchase Invoice created:",e)}).catch(e=>{console.error("Failed to approve purchase receipt:",e)}).finally(()=>{P.value=!1})};return(c,e)=>(d(),h(t(U),null,{default:a(()=>[s(F,{showBackButton:!0}),s(t(W),null,{default:a(()=>[s(t(V),null,{default:a(()=>[s(t(K),null,{default:a(()=>[s(t(L),{class:"flex justify-center"},{default:a(()=>[l(" Pembelian "+k(r.value.posting_date),1)]),_:1})]),_:1}),s(t(N),null,{default:a(()=>[s(t(O),null,{default:a(()=>[(d(!0),_(q,null,E(r.value.items,n=>(d(),h(t(B),{key:n.item_name},{default:a(()=>[s(t(g),null,{default:a(()=>[l(k(n.item_name),1)]),_:2},1024),s(t(g),null,{default:a(()=>[l(k(n.qty),1)]),_:2},1024),s(t(g),{class:"flex justify-end w-full text-right"},{default:a(()=>[l(k(n.amount),1)]),_:2},1024)]),_:2},1024))),128)),s(t(B),null,{default:a(()=>[s(t(g),null,{default:a(()=>[l("Total")]),_:1}),s(t(g),{class:"flex justify-end w-full text-right"},{default:a(()=>[l(k(r.value.total),1)]),_:1})]),_:1})]),_:1})]),_:1})]),_:1})]),_:1}),r.value.docstatus===0&&p.mode==="history"?(d(),h(t(u),{key:0,color:"danger",onClick:e[0]||(e[0]=n=>b.value=!0)},{default:a(()=>[l("Hapus Pengajuan")]),_:1})):f("",!0),r.value.docstatus===0&&p.mode==="history"?(d(),h(t(u),{key:1,onClick:e[1]||(e[1]=n=>m.value=!0)},{default:a(()=>[l("Ajukan Pembelian")]),_:1})):f("",!0),r.value.docstatus===1&&r.value.status=="To Bill"&&p.mode==="history"?(d(),h(t(u),{key:2,color:"danger",onClick:e[2]||(e[2]=n=>y.value=!0)},{default:a(()=>[l("Batalkan Pembelian")]),_:1})):f("",!0),r.value.docstatus===1&&r.value.status=="To Bill"&&p.mode==="approve"?(d(),h(t(u),{key:3,color:"success",onClick:e[3]||(e[3]=n=>x.value=!0)},{default:a(()=>[l("Setujui")]),_:1})):f("",!0),r.value.docstatus===1&&r.value.status=="To Bill"&&p.mode==="approve"?(d(),h(t(u),{key:4,color:"danger",onClick:e[4]||(e[4]=n=>C.value=!0)},{default:a(()=>[l("Tolak Pengajuan")]),_:1})):f("",!0),s(H),b.value?(d(),_("div",ee,[o("div",te,[ae,se,o("div",le,[s(t(u),{color:"danger",onClick:e[5]||(e[5]=n=>$(t(i).currentRoute.value.params.id))},{default:a(()=>[l("Hapus")]),_:1}),s(t(u),{onClick:e[6]||(e[6]=n=>b.value=!1)},{default:a(()=>[l("Batal")]),_:1})])])])):f("",!0),m.value?(d(),_("div",oe,[o("div",ne,[ue,ie,o("div",re,[s(t(u),{onClick:e[7]||(e[7]=n=>T(t(i).currentRoute.value.params.id))},{default:a(()=>[l("Ajukan")]),_:1}),s(t(u),{onClick:e[8]||(e[8]=n=>m.value=!1)},{default:a(()=>[l("Batal")]),_:1})])])])):f("",!0),y.value?(d(),_("div",de,[o("div",ce,[fe,pe,o("div",me,[s(t(u),{color:"danger",onClick:e[9]||(e[9]=n=>R(t(i).currentRoute.value.params.id))},{default:a(()=>[l("Batalkan")]),_:1}),s(t(u),{onClick:e[10]||(e[10]=n=>y.value=!1)},{default:a(()=>[l("Tutup")]),_:1})])])])):f("",!0),x.value?(d(),_("div",ve,[o("div",he,[_e,be,s(t(G),{modelValue:j.value,"onUpdate:modelValue":e[11]||(e[11]=n=>j.value=n)},{default:a(()=>[s(t(I),{value:"Wire Transfer","label-placement":"end"},{default:a(()=>[l("Bank")]),_:1}),ke,s(t(I),{value:"Cash","label-placement":"end"},{default:a(()=>[l("Kas")]),_:1})]),_:1},8,["modelValue"]),o("div",ge,[s(t(u),{onClick:A},{default:a(()=>[l("Lanjut")]),_:1}),s(t(u),{onClick:e[12]||(e[12]=n=>x.value=!1)},{default:a(()=>[l("Tutup")]),_:1})])])])):f("",!0),P.value?(d(),_("div",ye,[o("div",xe,[we,Pe,o("div",Ce,[s(t(u),{color:"success",onClick:e[13]||(e[13]=n=>M(t(i).currentRoute.value.params.id))},{default:a(()=>[l("Setujui")]),_:1}),s(t(u),{onClick:e[14]||(e[14]=n=>c.showApproveMOdal=!1)},{default:a(()=>[l("Tutup")]),_:1})])])])):f("",!0),C.value?(d(),_("div",je,[o("div",Re,[Be,Ie,o("div",$e,[s(t(u),{color:"danger",onClick:e[15]||(e[15]=n=>R(t(i).currentRoute.value.params.id))},{default:a(()=>[l("Tolak")]),_:1}),s(t(u),{onClick:e[16]||(e[16]=n=>C.value=!1)},{default:a(()=>[l("Tutup")]),_:1})])])])):f("",!0)]),_:1}))}};export{He as default};
