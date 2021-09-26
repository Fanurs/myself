<template>
  <footer
    v-if="$slidev.nav.currentLayout !== 'cover'"
    class="absolute top-0 right-0 p-0.5 text-xs bg-lime-300 opacity-50 rounded"
  >
    @Fanurs {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </footer>
</template>