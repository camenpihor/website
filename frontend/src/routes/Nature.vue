<template>
  <div class="nature">
    <ClientSideSearch
      class="nature__search"
      :keys="searchKeys"
      :json="natureItems"
      :jsonUUID="searchUUID"
      v-on:output="searchResults = $event"
    />

    <div v-if="searchResults.length > 0" class="nature__items">
      <b-tabs position="is-centered">
        <template v-for="(groupData, groupLabel, index) in groupedItems">
          <b-tab-item class="nature_item" :key="index" :label="groupLabel">
            <div class="nature__group columns is-multiline">
              <div
                class="nature__group__item column is-half"
                v-for="item in groupData"
                :key="item.label"
              >
                <div class="card">
                  <b-carousel
                    v-if="item.images.length > 1"
                    :autoplay="false"
                    :indicator="false"
                    icon-pack="fal"
                  >
                    <b-carousel-item
                      v-for="(filename, idx) in item.images"
                      :key="idx"
                    >
                      <div class="card-image">
                        <figure class="image is-4by3">
                          <img :src="getImageURL(filename)" />
                        </figure>
                      </div>
                    </b-carousel-item>
                  </b-carousel>
                  <div v-else class="card-image">
                    <figure class="image is-4by3">
                      <img :src="getImageURL(item.images[0])" />
                    </figure>
                  </div>

                  <div class="card-content">
                    <div class="media">
                      <div class="media-content">
                        <p class="title is-4">
                          <a v-if="item.url != ''" :href="item.url">{{
                            item.name
                          }}</a>
                          <span v-else>{{ item.name }}</span>
                          <span v-if="item.aka != ''" class="title is-6">
                            ({{ item.aka }})</span
                          >
                        </p>
                        <p v-if="item.group != ''" class="subtitle is-6">
                          {{ item.group }}
                        </p>
                      </div>
                    </div>

                    <div class="content">
                      <div v-if="item.location != ''">
                        <span class="bold">Location: </span>
                        <span class="light">{{ item.location }}</span>
                      </div>
                      <div v-if="item.native != ''">
                        <span class="bold">Native: </span>
                        <span class="light">{{ item.native }}</span>
                      </div>
                      <div v-if="item.identification != ''">
                        <span class="bold">Identification: </span>
                        <span class="light">{{ item.identification }}</span>
                      </div>
                      <div v-if="item.personal_notes != ''">
                        <span class="bold">Personal Notes: </span>
                        <span class="light">{{ item.personal_notes }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </b-tab-item>
        </template>
      </b-tabs>
    </div>
    <NoResults v-else message="No Results :(" />
  </div>
</template>

<script>
import ClientSideSearch from "@/components/search/ClientSideSearch.vue";
import NoResults from "@/components/NoResults.vue";

import natureIdentificationJson from "@/assets/json/nature_identification.json";
import { groupBy } from "@/assets/js/utilities.js";

export default {
  components: {
    ClientSideSearch,
    NoResults
  },
  data() {
    return {
      natureItems: natureIdentificationJson,
      searchResults: natureIdentificationJson,
      searchKeys: [
        "kind",
        "name",
        "group",
        "aka",
        "personal_notes",
        "notes",
        "identification"
      ],
      searchUUID: "name"
    };
  },
  computed: {
    groupedItems() {
      return groupBy(this.searchResults, "kind");
    }
  },
  methods: {
    getImageURL: function(filename) {
      if (filename != null) {
        return require(`@/assets/images/nature_identification/${filename}`);
      } else {
        return "https://bulma.io/images/placeholders/1280x960.png";
      }
    }
  }
};
</script>

<style>
.nature {
  max-width: 90vw;
}

.tabs {
  margin-left: auto;
  margin-right: auto;
  max-width: 700px;
}

.bold {
  font-weight: bold;
}

.light {
  font-weight: lighter;
}

.nature__search {
  margin-left: auto;
  margin-right: auto;
}

.nature__items {
  margin-top: 1rem;
}

.nature__group {
  margin-top: 3rem;
}

.nature__group__header {
  text-transform: capitalize;
  font-size: 1.5rem;
  font-weight: bold;
}

.nature__group__item {
  margin-bottom: 5rem;
}
</style>
