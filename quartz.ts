import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

import * as ExternalPlugin from "./.quartz/plugins";
import type { ExplorerOptions } from "./.quartz/plugins";

const explorerPrefixes: ExplorerOptions["mapFn"] = (node) => {
  if (node.isFolder) {
    node.displayName = ` ${node.displayName}`;
  } else {
    node.displayName = ` ${node.displayName}`;
  }
  return node;
}

ExternalPlugin.Explorer({
  mapFn: explorerPrefixes,
});

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
