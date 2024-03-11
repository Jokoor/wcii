function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["../nodes/0.qCVtzyJT.js","../chunks/scheduler.4DhuARt3.js","../chunks/index.DFJT2Gwo.js","../chunks/stores.76aYvh_a.js","../chunks/entry.Bxr674mu.js","../chunks/index.Cg4H_IDR.js","../chunks/Button.BqUzGTIN.js","../chunks/tw-merge.QHD3kepf.js","../chunks/prefers-reduced-motion.DXu69rMB.js","../chunks/Container.B28MuDHi.js","../assets/0.C2Yrshq-.css","../nodes/1.C-mLC1Bf.js","../nodes/2.CRptN_hU.js","../nodes/3.B7aWP7IQ.js","../nodes/4.Ciq3ioj2.js","../nodes/5.BLlLdsR6.js","../assets/5.BKVVyBHq.css","../nodes/6.qpJnYPoV.js"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
import{s as B,a as U,m as p,g as q,i as E,f as h,K as M,L as j,e as J,c as K,b as W,l as D,D as d,t as z,d as F,j as G,J as I,M as k,N as H}from"../chunks/scheduler.4DhuARt3.js";import{S as Q,i as X,b as g,e as L,t as w,g as P,c as v,a as O,m as R,d as y}from"../chunks/index.DFJT2Gwo.js";const Y="modulepreload",Z=function(a,e){return new URL(a,e).href},T={},b=function(e,n,i){let s=Promise.resolve();if(n&&n.length>0){const c=document.getElementsByTagName("link");s=Promise.all(n.map(t=>{if(t=Z(t,i),t in T)return;T[t]=!0;const r=t.endsWith(".css"),l=r?'[rel="stylesheet"]':"";if(!!i)for(let u=c.length-1;u>=0;u--){const m=c[u];if(m.href===t&&(!r||m.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${t}"]${l}`))return;const o=document.createElement("link");if(o.rel=r?"stylesheet":Y,r||(o.as="script",o.crossOrigin=""),o.href=t,document.head.appendChild(o),r)return new Promise((u,m)=>{o.addEventListener("load",u),o.addEventListener("error",()=>m(new Error(`Unable to preload CSS for ${t}`)))})}))}return s.then(()=>e()).catch(c=>{const t=new Event("vite:preloadError",{cancelable:!0});if(t.payload=c,window.dispatchEvent(t),!t.defaultPrevented)throw c})},re={};function $(a){let e,n,i;var s=a[1][0];function c(t,r){return{props:{data:t[3],form:t[2]}}}return s&&(e=k(s,c(a)),a[12](e)),{c(){e&&v(e.$$.fragment),n=p()},l(t){e&&O(e.$$.fragment,t),n=p()},m(t,r){e&&R(e,t,r),E(t,n,r),i=!0},p(t,r){if(r&2&&s!==(s=t[1][0])){if(e){P();const l=e;g(l.$$.fragment,1,0,()=>{y(l,1)}),L()}s?(e=k(s,c(t)),t[12](e),v(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(s){const l={};r&8&&(l.data=t[3]),r&4&&(l.form=t[2]),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&h(n),a[12](null),e&&y(e,t)}}}function x(a){let e,n,i;var s=a[1][0];function c(t,r){return{props:{data:t[3],$$slots:{default:[ee]},$$scope:{ctx:t}}}}return s&&(e=k(s,c(a)),a[11](e)),{c(){e&&v(e.$$.fragment),n=p()},l(t){e&&O(e.$$.fragment,t),n=p()},m(t,r){e&&R(e,t,r),E(t,n,r),i=!0},p(t,r){if(r&2&&s!==(s=t[1][0])){if(e){P();const l=e;g(l.$$.fragment,1,0,()=>{y(l,1)}),L()}s?(e=k(s,c(t)),t[11](e),v(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(s){const l={};r&8&&(l.data=t[3]),r&8215&&(l.$$scope={dirty:r,ctx:t}),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&h(n),a[11](null),e&&y(e,t)}}}function ee(a){let e,n,i;var s=a[1][1];function c(t,r){return{props:{data:t[4],form:t[2]}}}return s&&(e=k(s,c(a)),a[10](e)),{c(){e&&v(e.$$.fragment),n=p()},l(t){e&&O(e.$$.fragment,t),n=p()},m(t,r){e&&R(e,t,r),E(t,n,r),i=!0},p(t,r){if(r&2&&s!==(s=t[1][1])){if(e){P();const l=e;g(l.$$.fragment,1,0,()=>{y(l,1)}),L()}s?(e=k(s,c(t)),t[10](e),v(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(s){const l={};r&16&&(l.data=t[4]),r&4&&(l.form=t[2]),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&h(n),a[10](null),e&&y(e,t)}}}function V(a){let e,n=a[6]&&A(a);return{c(){e=J("div"),n&&n.c(),this.h()},l(i){e=K(i,"DIV",{id:!0,"aria-live":!0,"aria-atomic":!0,style:!0});var s=W(e);n&&n.l(s),s.forEach(h),this.h()},h(){D(e,"id","svelte-announcer"),D(e,"aria-live","assertive"),D(e,"aria-atomic","true"),d(e,"position","absolute"),d(e,"left","0"),d(e,"top","0"),d(e,"clip","rect(0 0 0 0)"),d(e,"clip-path","inset(50%)"),d(e,"overflow","hidden"),d(e,"white-space","nowrap"),d(e,"width","1px"),d(e,"height","1px")},m(i,s){E(i,e,s),n&&n.m(e,null)},p(i,s){i[6]?n?n.p(i,s):(n=A(i),n.c(),n.m(e,null)):n&&(n.d(1),n=null)},d(i){i&&h(e),n&&n.d()}}}function A(a){let e;return{c(){e=z(a[7])},l(n){e=F(n,a[7])},m(n,i){E(n,e,i)},p(n,i){i&128&&G(e,n[7])},d(n){n&&h(e)}}}function te(a){let e,n,i,s,c;const t=[x,$],r=[];function l(o,u){return o[1][1]?0:1}e=l(a),n=r[e]=t[e](a);let _=a[5]&&V(a);return{c(){n.c(),i=U(),_&&_.c(),s=p()},l(o){n.l(o),i=q(o),_&&_.l(o),s=p()},m(o,u){r[e].m(o,u),E(o,i,u),_&&_.m(o,u),E(o,s,u),c=!0},p(o,[u]){let m=e;e=l(o),e===m?r[e].p(o,u):(P(),g(r[m],1,1,()=>{r[m]=null}),L(),n=r[e],n?n.p(o,u):(n=r[e]=t[e](o),n.c()),w(n,1),n.m(i.parentNode,i)),o[5]?_?_.p(o,u):(_=V(o),_.c(),_.m(s.parentNode,s)):_&&(_.d(1),_=null)},i(o){c||(w(n),c=!0)},o(o){g(n),c=!1},d(o){o&&(h(i),h(s)),r[e].d(o),_&&_.d(o)}}}function ne(a,e,n){let{stores:i}=e,{page:s}=e,{constructors:c}=e,{components:t=[]}=e,{form:r}=e,{data_0:l=null}=e,{data_1:_=null}=e;M(i.page.notify);let o=!1,u=!1,m=null;j(()=>{const f=i.page.subscribe(()=>{o&&(n(6,u=!0),H().then(()=>{n(7,m=document.title||"untitled page")}))});return n(5,o=!0),f});function N(f){I[f?"unshift":"push"](()=>{t[1]=f,n(0,t)})}function S(f){I[f?"unshift":"push"](()=>{t[0]=f,n(0,t)})}function C(f){I[f?"unshift":"push"](()=>{t[0]=f,n(0,t)})}return a.$$set=f=>{"stores"in f&&n(8,i=f.stores),"page"in f&&n(9,s=f.page),"constructors"in f&&n(1,c=f.constructors),"components"in f&&n(0,t=f.components),"form"in f&&n(2,r=f.form),"data_0"in f&&n(3,l=f.data_0),"data_1"in f&&n(4,_=f.data_1)},a.$$.update=()=>{a.$$.dirty&768&&i.page.set(s)},[t,c,r,l,_,o,u,m,i,s,N,S,C]}class oe extends Q{constructor(e){super(),X(this,e,ne,te,B,{stores:8,page:9,constructors:1,components:0,form:2,data_0:3,data_1:4})}}const ae=[()=>b(()=>import("../nodes/0.qCVtzyJT.js"),__vite__mapDeps([0,1,2,3,4,5,6,7,8,9,10]),import.meta.url),()=>b(()=>import("../nodes/1.C-mLC1Bf.js"),__vite__mapDeps([11,1,2,3,4,5]),import.meta.url),()=>b(()=>import("../nodes/2.CRptN_hU.js"),__vite__mapDeps([12,1,2,9,8,7,5]),import.meta.url),()=>b(()=>import("../nodes/3.B7aWP7IQ.js"),__vite__mapDeps([13,1,2,9]),import.meta.url),()=>b(()=>import("../nodes/4.Ciq3ioj2.js"),__vite__mapDeps([14,1,2]),import.meta.url),()=>b(()=>import("../nodes/5.BLlLdsR6.js"),__vite__mapDeps([15,1,2,9,6,7,16]),import.meta.url),()=>b(()=>import("../nodes/6.qpJnYPoV.js"),__vite__mapDeps([17,1,2]),import.meta.url)],le=[],fe={"/":[2],"/about-us":[4],"/contact":[5],"/e-library":[6],"/[program]~[course]":[-4]},ce={handleError:({error:a})=>{console.error(a)},reroute:()=>{}};export{fe as dictionary,ce as hooks,re as matchers,ae as nodes,oe as root,le as server_loads};
