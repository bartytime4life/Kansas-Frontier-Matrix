// TEST-ONLY: these mocks preserve the private-profile geometry/transport regression
// harnesses. They do not change the immutable public application profile or grant
// release authority. Public gating and withdrawal use the real profile separately.
export const PRIVATE_PROFILE_TEST_ONLY = Object.freeze({
  IS_PUBLIC_COPY: false,
  PUBLIC_RELEASE_RECHECK_MS: 60_000,
  publicDataAsset: path => path,
  publicContextSourceAllowed: () => true,
  publicBasemap: key => key,
  publicFamilyAvailable: async () => true,
  publicAssetLease: () => { throw new Error('Private regression harness must not use public release authority'); },
});

// ES-module equivalent for legacy transport and renderer harnesses.
export const PRIVATE_PROFILE_URL_TEST_ONLY = `data:text/javascript;base64,${Buffer.from(`
export const IS_PUBLIC_COPY = false;
export const PUBLIC_RELEASE_RECHECK_MS = 60000;
export const publicContextSourceAllowed = () => true;
export const publicBasemap = key => key;
export const publicDataAsset = path => path;
export const publicFamilyAvailable = async () => true;
export const publicAssetLease = () => { throw new Error('Private regression harness has no public release authority'); };
`).toString('base64')}`;
