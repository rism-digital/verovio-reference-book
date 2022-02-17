---
layout: book
title: Search results
hide_title: true
no-edit: true
---

{% assign search_results = "Search results" %}
{% assign search_no_result = "No result found when searching for" %}
{% assign search_no_query = "Enter a search term ..." %}
{% assign search_results_count = "result(s)" %}

<div id="search-results-header" style="display: none;">
    <h2>{{ search_results }}</h2>

    <p id="search-results-p" class="mb-5"><i><span id="search-results-count"></span> {{ search_results_count }}</i></p>
</div>


<div id="search-results">
</div>

<template id="search-item-template">
    <div class="mb-5">
        <h3 class="mb-1"><a></a></h3>
        <p class="post-info is-italic mb-1"></p>
        <p class="text"></p>
    </div>
</template>

<script src="/js/lunr.js"></script>

<script>

    // HTML element defined above
    let searchResults = document.querySelector( "#search-results" );
    let searchResultsHeader = document.querySelector( "#search-results-header" );
    let searchResultsP = document.querySelector( "#search-results-p" );
    let searchResultsCount = document.querySelector( "#search-results-count" );

    // Async Function to Start LunrJS
    async function startLunrJSAsync()
    {
        console.log( "search: Starting Lunr..." );

        let idx, pages;
        let ok = false;

        const lunrPages = "/pages.json";

        // Load the Page Summaries
        console.log( "search: Fetching Pages..." );
        response = await fetch( lunrPages );
        pages = await response.json();
        console.log( "search: Pages Loaded!" );

        // Build the index
        idx = lunr( function ()
        {
            this.ref( 'id' )
            this.field( 'title' )
            this.field( 'body' )

            pages.forEach( function ( doc )
            {
                this.add( doc )
            }, this )
        } );

        // Lunr is Ready; Return */
        console.log( "search: Lunr Is Ready!" );
        ok = true;
        let obj = {
            idx: idx,
            pages: pages,
            ok: ok
        };
        return obj;
    }

    // Clear the Search Results element then populate with search results
    function searchSite( search, query, query_term )
    {
        let template = document.querySelector( "#search-item-template" );

        let allResults = search.idx.search( query );

        if ( allResults.length === 0 ) {
            searchResultsP.innerHTML = "{{ search_no_result }} '" + query_term + "'";
        }
        else {
            searchResultsCount.innerHTML = allResults.length;
            allResults.forEach( function ( result )
            {
                let output = document.importNode( template.content, true );
                let title = output.querySelector( "a" );
                let summary = output.querySelector( "p.text" );
                let docRef;

                // Find the requisite document summary for the search result
                for ( let i = 0; i < search.pages.length; i++ )
                {
                    if ( search.pages[i].id == result.ref )
                    {
                        docRef = search.pages[i];
                        break;
                    }
                }
                if ( docRef )
                {
                    title.innerHTML = docRef.title;
                    title.setAttribute( "href", docRef.url );
                    summary.innerHTML = docRef.body.substring( 0, 200 ) + '...';
                    searchResults.appendChild( output );
                }
            } );
        }
    }

    ( async () =>
    {
        // Initialize Lunr
        let Search = await startLunrJSAsync();

        // Hide the progress bar
        searchResults.innerHTML = "";
        
        // HTML elements from the sidebar (if any) - these can be undefined
        let searchForm = document.getElementById("website-search");

        let params = new URLSearchParams( document.location.search.substring( 1 ) );
        if ( params.get( "q" ) )
        {
            let query = params.get( "q" );
            // Also make sure we preserve the query term in the form
            // This can be in the navbar or in the sidebar
            document.getElementById("website-search").value = query;
            // Preserve the original query for logging
            let query_term = query;
            // Remove quotes and trim
            query = query.replace(/\'|\"/g, ' ');
            query = query.trim();
            // Make it an AND query
            query = query.replace(/\s+/g, ' +');
            if (!query.startsWith("+")) {
                query = "+" + query;
            }
            console.log(query);
            //console.log( query )
            searchSite( Search, query, query_term );
        }
        else {
            // Display message to enter a query
            searchResultsP.innerHTML = "{{ search_no_query }}";
        }
        // Show the header with the message (result count, no query or no result)
        searchResultsHeader.style.display = "block";
    } )();
</script>
