import { fetchRuling } from "$lib/scripts/fetchRuling.js";
import { fail } from "@sveltejs/kit";
import { PUBLIC_SERVER_API_URL } from '$env/static/public';


const fetchFavorite = async (rulingId, cookie) => {

    let response;
    try {

        response = await fetch(
            `${PUBLIC_SERVER_API_URL}/favorites/isFavorite/${rulingId}/`,
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': cookie },
            }
        );

    } catch (err) { throw new Error(err); }

    return response.status === 200;

}

export async function load({ params, locals, cookies }) {

    const ruling = await fetchRuling(params.ruling);


    const auth = cookies.get('AuthorizationToken');

    let isFavorited = false;
    if (auth) {
        isFavorited = await fetchFavorite(params.ruling, auth);
    }

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    let versions = ruling.slice(0, -1);

    return {
        ruling: ruling[ruling.length - 1],
        versions: versions,
        user: user,
        favorite: isFavorited
    };
}

export const actions = {

    favorite: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await event.request.formData();

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_SERVER_API_URL}/favorites/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify({
                            acordao: data.get('id'),
                            description: data.get('description')
                        })
                    });

            } catch (err) {
                return fail(500, "Server is down.");
            }

            if (!response.ok) {
                const data = await response.json();
                return fail(400, data.toString());
            }
        }
    },

    suggest: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await event.request.formData();
            const id = data.get('id');

            let dataAsJson = {"Descritores": []};

            data.forEach((value, key) => {

                if (key.includes("Descritores[")) {
                    dataAsJson["Descritores"].push(value)
                }
                else if (!Reflect.has(dataAsJson, key)){
                    dataAsJson[key] = value;
                }

            });

            delete dataAsJson.id;

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_SERVER_API_URL}/acordaos/changeRequests/${id}/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(dataAsJson)
                    });

            } catch (err) {
                return fail(500, "Server is down.");
            }

            if (!response.ok) {
                const data = await response.json();
                return fail(400, data.toString());
            }
        }
    },


};