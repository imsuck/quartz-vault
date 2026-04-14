import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "imsuck's vault",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "imsuck.vercel.app",
    ignorePatterns: ["99 Templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Sans",
        body: "Lexend",
        code: "Fira Code",
      },
      colors: {
        lightMode: {
          light: "#eff1f5",        // base
          lightgray: "#acb0be",    // mantle
          gray: "#bcc0cc",         // overlay1
          darkgray: "#4c4f69",     // text
          dark: "#2b2c3b",         // text with 20% lightness

          secondary: "#1e66f5",    // blue
          tertiary: "#40a02b",     // green

          highlight: "rgba(30, 102, 245, 0.12)",  // blue w/ alpha
          textHighlight: "#df8e1d88"              // yellow w/ alpha
        },

        darkMode: {
          light: "#24273a",        // base
          lightgray: "#363a4f",    // surface0
          gray: "#6e738d",         // overlay0
          darkgray: "#cad3f5",     // text
          dark: "#f4dbd6",         // rosewater

          secondary: "#8aadf4",    // blue
          tertiary: "#a6da95",     // green

          highlight: "rgba(138, 173, 244, 0.16)", // blue w/ alpha
          textHighlight: "#eed49f88"              // yellow w/ alpha
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "catppuccin-latte",
          dark: "catppuccin-macchiato",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "typst" }),
    ],
    filters: [Plugin.ExplicitPublish()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
