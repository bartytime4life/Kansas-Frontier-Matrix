// Bounded allowances for one GPU generation plus up to two waiting requests.
// The poll transport returns jobs promptly; none of these is a browser HTTP hold.
export const INFERENCE_BUDGETS=Object.freeze({
 runMs:210000,queueSlotMs:215000,queueMs:430000,
 gatewayMs:640000,relayMs:650000,workerMs:660000,clientMs:670000,
 jobMs:700000,publicSlots:3,retentionMs:900000,
});
