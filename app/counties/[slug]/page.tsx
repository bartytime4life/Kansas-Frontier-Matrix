import { COUNTY_PAGES } from "../../county-pages";
import { CountyPage, countyMetadata } from "../county-page";

type Props = { params: Promise<{ slug: string }> | { slug: string } };

export function generateStaticParams() { return COUNTY_PAGES.map(county => ({ slug: county.slug })); }
export async function generateMetadata({ params }: Props) { return countyMetadata((await params).slug); }
export default async function Page({ params }: Props) { return <CountyPage slug={(await params).slug} />; }
