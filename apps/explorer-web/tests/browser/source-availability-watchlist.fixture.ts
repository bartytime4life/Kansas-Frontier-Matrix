import invalidFixture from "../../../../fixtures/ui/source_availability_watchlist_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/source_availability_watchlist_projection/valid/available.json";
import { mountSourceAvailabilityWatchlist } from "../../src/features/source_availability_watchlist";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Source availability watchlist fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountSourceAvailabilityWatchlist(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
