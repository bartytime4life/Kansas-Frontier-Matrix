declare module "lerc" {
  const Lerc: {
    decode(input: ArrayBuffer): {
      width: number;
      height: number;
      pixels: ArrayLike<ArrayLike<number>>;
      mask?: ArrayLike<number>;
    };
  };
  export default Lerc;
}
