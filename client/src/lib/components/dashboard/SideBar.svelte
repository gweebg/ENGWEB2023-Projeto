<script>

    import SideBarItem from "$lib/components/dashboard/SideBarItem.svelte";

    export let active;
    export let name = "The best rulings database.";
    export let basePath = "";
    export let isAdmin;

</script>

<div class="text-base-100 bg-neutral h-screen w-96 p-5 pt-8 flex flex-col custom">

    <div class="flex justify-between items-center px-2">

        <div>
            <h1 class="normal-case text-2xl ml-0 font-semibold">Accordb</h1>
            <p class="opacity-40">{name}</p>
        </div>

        <a href="/home" class="btn btn-circle btn-neutral">
            <img src="/icons/menu/arrow-left.svg" alt="Back Arrow">
        </a>

    </div>

    <div class="divider border-t border-white"></div>

    <!-- Menu Items -->
    <div class="flex flex-col gap-2 flex-grow">

        <!-- If user is administrator -->
        {#if isAdmin}

            <SideBarItem params={{text: "Perfil", iconPath: "/icons/menu/profile.svg", isActive: active.profile, link: `${basePath}/profile`}}/>
            <SideBarItem params={{text: "Favoritos", iconPath: "/icons/menu/favourites.svg", isActive: active.favourites, link: `${basePath}/favorites`}}/>
            <SideBarItem params={{text: "Pedidos de Revisão", iconPath: "/icons/menu/request_in.svg", isActive: active.requests, link: `${basePath}/requests`}}/>

            <div class="divider border-t border-white mb-1"></div>

            <SideBarItem params={{text: "Adicionar Novo Acórdão", iconPath: "/icons/menu/add.svg", isActive: active.add, link: "/new"}}/>

        {:else}

            <SideBarItem params={{text: "Perfil", iconPath: "/icons/menu/profile.svg", isActive: active.profile, link: `${basePath}/profile`}}/>
            <SideBarItem params={{text: "Favourites", iconPath: "/icons/menu/favourites.svg", isActive: active.favourites, link: `${basePath}/favorites`}}/>
            <SideBarItem params={{text: "Pedidos de Revisão", iconPath: "/icons/menu/request_out.svg", isActive: active.requests, link: `${basePath}/requests`}}/>

            <div class="divider border-t border-white mb-1"></div>

        {/if}


    </div>


    <!-- End Items -->
    <div>

        <div class="divider border-t border-white mb-1"></div>

        <form action="/logout" method="POST" class="h-full w-full">
            <button type="submit" class="btn btn-neutral w-full gap-4 text-base-100-focus float-right hover:bg-error text-left justify-start items-center">
                <img src="/icons/menu/logout.svg" alt="Logout">
                Logout
            </button>
        </form>

    </div>


</div>


<style>

    .custom {
        box-shadow: 1px 0 20px 5px rgba(0, 0, 0, 0.3);
    }

</style>