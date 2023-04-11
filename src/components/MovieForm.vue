<template>
        <form action="POST" @submit.prevent="saveMovie" id = "Movie-Form" enctype="multipart/form-data">
                <label for="title" class="sub">Movie Title</label><br>
                <input type="text" name="title" class="form-control" />
                <br>
                <label for="description" class="sub">Description</label><br>
                <input type="text" name="description" class="form-control" />
                <br>
                <label for="poster"  class="sub">Movie Poster</label><br>
                <input type="file" name="poster" id = "image-file" class="form-control" />
                <br><br>
                <input type="submit" value="Submit">
        </form>
</template>

<script setup>
    import { ref, onMounted } from "vue";
    onMounted(() => {
    getCsrfToken();
    });
    function saveMovie() {
        let MovieForm = document.getElementById('Movie-Form');
        let form = new FormData(Movie-Form);
        fetch("/api/v1/movies", {
        method: 'POST',
        body: form,
    headers: {
    'X-CSRFToken': csrf_token.value
    }
        })
        .then(function (response) {
        return response.json();
        })
        .then(function (data) {
        // display a success message
        console.log(data);
        })
        .catch(function (error) {
        console.log(error);
        });
    }
    let csrf_token = ref("");
        function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
    }
</script>