import{E as _,_ as v,D as C,a as r,o as u,b as c,Q as k,R as h,S as x,e as t,w as l,d as w,f as n,t as B,i as y,x as p,Z as U}from"./index.87eb2f25.js";import{F}from"./FileUploader.3e02f4ff.js";const S={name:"InsertImage",props:["editor"],expose:["openDialog"],data(){return{addVideoDialog:{url:"",file:null,show:!1}}},components:{Button:v,Dialog:C,FileUploader:F},methods:{openDialog(){this.addVideoDialog.show=!0},onVideoSelect(i){let o=i.target.files[0];!o||(this.addVideoDialog.file=o)},addVideo(i){this.editor.chain().focus().insertContent(`<video src="${i}"></video>`).run(),this.reset()},reset(){this.addVideoDialog=this.$options.data().addVideoDialog}}},I={class:"flex items-center space-x-2"},N=["src"];function A(i,o,R,b,e,a){const s=r("Button"),f=r("FileUploader"),V=r("Dialog");return u(),c(U,null,[k(i.$slots,"default",h(x({onClick:a.openDialog}))),t(V,{options:{title:"Add Video"},modelValue:e.addVideoDialog.show,"onUpdate:modelValue":o[2]||(o[2]=d=>e.addVideoDialog.show=d),onAfterLeave:a.reset},{"body-content":l(()=>[t(f,{"file-types":"video/*",onSuccess:o[0]||(o[0]=d=>e.addVideoDialog.url=d.file_url)},{default:l(({file:d,progress:g,uploading:m,openFileSelector:D})=>[w("div",I,[t(s,{onClick:D},{default:l(()=>[n(B(m?`Uploading ${g}%`:e.addVideoDialog.url?"Change Video":"Upload Video"),1)]),_:2},1032,["onClick"]),e.addVideoDialog.url?(u(),y(s,{key:0,onClick:()=>{e.addVideoDialog.url=null,e.addVideoDialog.file=null}},{default:l(()=>[n(" Remove ")]),_:2},1032,["onClick"])):p("",!0)])]),_:1}),e.addVideoDialog.url?(u(),c("video",{key:0,src:e.addVideoDialog.url,class:"mt-2 w-full rounded-lg",type:"video/mp4",controls:""},null,8,N)):p("",!0)]),actions:l(()=>[t(s,{variant:"solid",onClick:o[1]||(o[1]=d=>a.addVideo(e.addVideoDialog.url))},{default:l(()=>[n(" Insert Video ")]),_:1}),t(s,{onClick:a.reset},{default:l(()=>[n("Cancel")]),_:1},8,["onClick"])]),_:1},8,["modelValue","onAfterLeave"])],64)}var P=_(S,[["render",A]]);export{P as default};
