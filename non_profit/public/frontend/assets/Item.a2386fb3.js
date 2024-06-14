import{c as t,Z as a}from"./index.92312bcf.js";t({url:"non_profit.api.fundraising.get_item_group",auto:!0,transform(r){for(let o in r)u.push(r[o])}});const u=a([]);function p(r){return new Promise((o,s)=>{t({method:"POST",url:"non_profit.api.fundraising.add_item_group",params:{item_group_name:r},onSuccess:e=>{console.log("New item group created:",e),o(e)},onError:e=>{console.error("Error creating new item group:",e),s(e)}}).reload()})}function d(r){return new Promise((o,s)=>{t({method:"POST",url:"non_profit.api.fundraising.delete_item_groups",params:{item_groups:r},onSuccess:e=>{console.log("Item group deleted:",e),o(e)},onError:e=>{console.error("Error deleting item group:",e),s(e)}}).reload()})}t({url:"non_profit.api.fundraising.get_asset_category",auto:!0,transform(r){for(let o in r)c.push(r[o])}});const c=a([]);function f(r){return new Promise((o,s)=>{t({method:"POST",url:"non_profit.api.fundraising.add_asset_category",params:{asset_category:r},onSuccess:e=>{console.log("New asset category created:",e),o(e)},onError:e=>{console.error("Error creating new asset category:",e),s(e)}}).reload()})}function _(r){return new Promise((o,s)=>{t({method:"POST",url:"non_profit.api.fundraising.delete_asset_categories",params:{asset_categories:r},onSuccess:e=>{console.log("Asset category deleted:",e),o(e)},onError:e=>{console.error("Error deleting asset category:",e),s(e)}}).reload()})}const w=(r=null,o=null)=>{let s={};r&&(s.item_group=r),r==="Aset Tetap"&&o&&(s.asset_category=o),t({url:"non_profit.api.fundraising.get_item",params:s,transform(e){console.log(e);for(let n in e)l.push(e[n])}}).reload()},l=a([]);t({url:"non_profit.api.fundraising.get_uom",auto:!0,transform(r){for(let o in r)m.push(r[o])}});const m=a([]);function h(r,o){return new Promise((s,i)=>{t({method:"POST",url:"non_profit.api.fundraising.add_item",params:{item_group:r,item:o},onSuccess:n=>{console.log("New item created:",n),s(n)},onError:n=>{console.error("Error creating new item:",n),i(n)}}).reload()})}export{p as a,w as b,l as c,d,c as e,f,_ as g,h,u as i,m as u};
