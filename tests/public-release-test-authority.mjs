// TEST ONLY. This substitutes an already-authorized upstream boundary for the
// inherited family-adapter fixtures. It is never a deployment allowlist or pin.
// The real public compiler/runtime/auth/withdrawal path is exercised separately
// in public-release.test.mjs with its explicit synthetic contract fixtures.
export async function publicFixtureAuthority(packages, waterUrl) {
  const allowed = await Promise.all(packages.map(async ({family,raw,decision}) => ({
    family, package_id: decision.package_id, sha256: "sha256:" + [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(raw)))].map(n=>n.toString(16).padStart(2,"0")).join(""), decision,
  })));
  const source = `
    import {canonical,digest} from ${JSON.stringify(waterUrl)};
    const allowed=${JSON.stringify(allowed)};
    export class PublicReleaseError extends Error {constructor(reason,status=503){super(reason);this.status=status;}}
    export async function publicFamilyAuthorization(family,id,raw,decision){
      const item=allowed.find(item=>item.family===family&&item.package_id===id);
      if(!item||await digest(raw)!==item.sha256||canonical(decision)!==canonical(item.decision))throw new PublicReleaseError('SYNTHETIC_PUBLIC_BINDING_MISMATCH');
      return item;
    }
    export async function publicStageAuthorization(family,raw){
      const item=allowed.find(item=>item.family===family&&item.package_id===JSON.parse(raw).manifest.package_id);
      if(!item||await digest(raw)!==item.sha256)throw new PublicReleaseError('SYNTHETIC_PUBLIC_BINDING_MISMATCH');
      return item;
    }
    export async function publicDecisionForActivation(family,id){
      const item=allowed.find(item=>item.family===family&&item.package_id===id);
      if(!item)throw new PublicReleaseError('SYNTHETIC_PUBLIC_BINDING_MISMATCH');
      return item.decision;
    }
    export async function publicAuthorizedPackages(family){return (await publicAuthorizationStatus(family)).authorized_packages;}
    export async function publicAuthorizationStatus(family){
      const candidates=allowed.filter(item=>item.family===family), authorized_packages=candidates.filter(item=>Date.now()<Date.parse(item.decision.expires_at)).map(item=>({package_id:item.package_id,expires_at:item.decision.expires_at}));
      return {authorized_packages,release_hold:authorized_packages.length?null:candidates.length?'PUBLIC_RELEASE_EXPIRED':'NO_APPROVED_PUBLIC_RELEASE'};
    }
  `;
  return "data:text/javascript;base64,"+Buffer.from(source).toString("base64");
}
