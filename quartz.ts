import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

import { Explorer, ExplorerOptions } from "@quartz-community/explorer"

const explorerPrefixes: ExplorerOptions["mapFn"] = (node) => {
  if (!node.isFolder) {
    node.displayName = ` ${node.displayName}`
  }
  return node
}

Explorer({
  mapFn: explorerPrefixes,
})

// author: https://github.com/fanteastick
const possiblePageTitles = [
  "(｡•ㅅ•｡)~✧",
  "૭( ᵕ•̀ᵕ•́૭)",
  "(૭ •́ ᵕ•̀ )૭",
  "(๑>؂·̀๑)",
  "৻(•̀ᗜ•́৻)",
  "٩(•̤̀ᵕ•̤́๑)",
  "(｡•́︿•̀｡)",
  "ᕙ( •̀ ᗜ •́ )ᕗ",
  "(๑•́ ₃ •̀๑)",
  "(づ ̄ ³ ̄)づ",
  "( ˵ •̀ ᴗ •́˵)",
  "(๑•́o•̀๑)",
  "٩(๑❛ᴗ❛๑)6",
  "(╥﹏╥)",
  "( ˘ ³˘(◡‿◡˶)",
  "٩(๑˘•ω•˘๑)٩",
  "૮ ˶ᵔ ᵕ ᵔ˶ ა",
  "(˶˃ ᵕ ˂˶).ᐟ",
  "ദ്ദി •⩊• )",
  "꒰ᐢ. .ᐢ꒱₊˚⊹",
  "˚ʚ♡ɞ˚",
  "⸜(｡˃ ᵕ ˂ )⸝♡",
  "`⎚⩊⎚´ -✧",
  "(˶˃ ᵕ ˂˶)~✧",
  "(˵•̀ ᴗ •́˵)~✧",
  "(૮ ᵕ•̀ )૮~✧",
  "一人一つ",
]
function getRandomPageTitle(): string {
  return possiblePageTitles[Math.floor(Math.random() * possiblePageTitles.length)]
}

const config = await loadQuartzConfig({
  pageTitle: getRandomPageTitle(),
})
export default config
export const layout = await loadQuartzLayout()
