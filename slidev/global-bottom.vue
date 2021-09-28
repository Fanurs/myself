<template>
  <footer
    v-if="$slidev.nav.currentLayout !== 'cover'"
    class="absolute top-0 right-0 p-0.5 text-xs"
  >
    <a href="https://fanurs.github.io/myself/" title="Personal homepage">@Fanurs</a> {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </footer>
</template>