from discord.ext import commands
from aternosapi import AternosAPI

TOKEN = "TsSZxZQ3vtKEYuBPKdNA"
HEADER_TOKEN = "ATERNOS_SEC_9tncd7amkc600000=11gtn2qtvxfe0000; __cfduid=d76da08b4c04b98cc54b239488d7772971610024571; _ga=GA1.2.1781703978.1610024573; _gid=GA1.2.1518853503.1610024573; ATERNOS_SESSION=kmxjT5LysFZKZJgw71VnlvLh3sthRiZc7ILMaKewfvWTa1yYwEVqUPwco5TwgO3eSM8VzXHxqmq8wrHsdswPm3sN2m3GDHwjyzjF; ATERNOS_SERVER=wlL0kmOfiyRPv12N; snconsent=eyJwdWJsaXNoZXIiOjAsInZlbmRvciI6MywiZ2xDb25zZW50cyI6IiIsImN2Q29uc2VudHMiOnt9fQ.AocAJwArAC4ANwA9AEIARgBTAFkAXQBsAHUAegB8AIMAhwCIAI8AkACTAJUAnwCiAKcAqwC4AMAAxADKANMA2gDkAOYA7wDxAP0BAwEKARABHgEjATcBPQFCAUMBRgFHAVIBbwFzAYEBhQGJAYoBjQGXAZ0BnwGoAa4BtAG4Ab0BwAHBAcUB4gHmAesB7gHvAfUB9wH5AgoCCwIcAiYCLwIwAjgCOwI-AkACSAJJAksCTwLdAuEC6QMMAxMDIgMjAzEDNAM1Az0DRwNVA2ADYwNqA4MDiAOaA6MDqgPTA9UD2QPrBAAEAwQHBAkECgQQBBYEGwQdBCsEPQREBEcESQRLBFMEZgRnBG8EdwR9BIAEigSOBJMEogSkBKgEsQS0BLUEuwS_BMoEywTOBOAE5AT0BPYE_AUEBQYFCgUVBRsFIAUlBTEFQQVMBVQFVQVfBXsFgwWHBYgFiwWgBaIFqQWvBbAFuQXXBegF7AX1BgQGDAYTBhYGHAYiBikGKwYvBjAGNwZDBlAGZgZzBnUGgQaDBocGjQaOBpIGoQajBqcGsAa0BrkGuga9BsQG0QbWBtkG5QbpBvYG-gcIBxAHEgchByMHKActBy4HMAcyBzMHNAc1B0MHSgdOB1YHWAdhB2oHawd9B4kHlgeYB6oHqwesB68HsAexB7oHzgfTB9cH3QfrB_MH9wf8B_8IBAgICBAIFAgWCBgIGggoCCoINwg7CD0IQwhMCFIIVQhZCFwIYQhjCGYIbAh2CIEIgwiHCIoImgidCKUIqAirCKwIrgixCLoIzQjYCOcI6gj0CPsJAQkFCQgJDAkVCRgJGwkeCR8JIAkhCScJMgk1CTYJNwk-CUIJSAlJCVMJWAlaCWAJYwllCWYJZwlrCW4JcAlyCXYJeQl7CYgJjwmbCZ0JngmkCagJrQmxCbQJtgm4CbwJvQnACcEJwgnDCcgJzgnPCdUJ3gnfCeQJ5gnnCe4J8An4CfsKAwoECgcKCAoJCgsKDAoPChEKFwoYCh0KIwokCikKLAotCjAKMQoyCjQKNgo9CkQKRQpJCkoKTApSClMKVQpWClcKWgpbClwKYAphCmIKZAplCm0KbgpxCnUKeQp8Cn4KfwqCCoMKhwqKCpMKmQqaCqkKswrPCtAK0grTCtQK4ArjCucK6AruCvEK9Qr8Cv0LAAsBCwILBQsGCwsLDgsPCxILFAsWCxcLGAscCx4LHwshCyILIwskCyYLKAssCy4LLwsxCzMLNQs5CzoLOws8Cz4LPwtAC0ELQgtDC0QLRQtGC0cLSAtJC0sLTQtOC08LUQtSC1QLVQtcC10LXwtgC2ELYgtkC2ULZgtnC2gLagtrC2wLbwtxC3ILcwt1C3sLfAt9C34LgwuFC4YLjAuRC5ILkwuUC5ULlguYC5kLmgudC54LnwujC6QLpQunC6kLqgurC68LsQuyC7MLtQu4C7oLuwu9C8ALwQvCC8MLxAvIC8kLygvLC9AL0QvZC9oL3QveC-ML5AvlC-gL6gvrC-wL7QvvC_IL8wv3C_kL-gv8C_4MAAwBDAIMAwwEDAUMBgwRDBIMFQwWDBcMGQwbDBwMIAwiDCQMJQwnDCgMLAwtDC4MLwwwDDEMNAw2DDcMOAw6DD8MQAxDDEkMTQxODE8MUgxTDFcMWgxbDF0MXwxkDGUMbAxuDG8McAxxDHIMcwx0DHUMdgx5DHoMfAx9DIkMigyLDI4MjwyR; euconsent-v2=CO_plWjO_plWjDlArAFRBHCsAP_AAH_AACiQHONf_X_fb3_j-_59__t0eY1f9_7_v-0zjheds-8Nyd_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6IlVrTPsbk2Mr7NKJ7PEmnsbe2dYGH9_n9XT_ZKZ79_v___7________77______3_v_____-___QOcAJMNS-AizEscCSaNKoUQIQriQ6AUAFFCMLRNYQErgp2VwEfoIGACA1ARgRAgxBRiwCAAAAAJKIgJADwQCIAiAQAAgBUgIQAEaAILACQMAgAFANCwAigCECQgyOCo5TAgIkWignkjAEou9jDCEMosAKBR_QAAA; id5id.1st_364_nb=0; __gads=ID=a6d7251b370f7f32:T=1610025106:S=ALNI_MZJtIA0BOdEiai8TVIvgXUgph7Y-g; _pbjs_userid_consent_data=5783328327091157; id5id.1st_212_nb=0; SKpbjs-unifiedid=%7B%22TDID%22%3A%227efeb93f-5187-4172-98a8-8a91abb1e1c4%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-12-07T13%3A11%3A58%22%7D; SKpbjs-unifiedid_last=Thu%2C%2007%20Jan%202021%2013%3A11%3A58%20GMT; SKpbjs-id5id=%7B%22created_at%22%3A%222021-01-07T13%3A11%3A58.243Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMON2rZn_THi2N9KwJQ_oEuFEHwbe-GDPKke8Q3jg%22%2C%22universal_uid%22%3A%22ID5-ZHMOTqMAI4CngepbqK1amWDC-6VqFKkrDPFSyo7c7A%22%2C%22signature%22%3A%22ID5_AaqHgwgnmS75-o1Lt4lHwDViNWHi9UG3gzUgWGI0SG46ROe2CNPetsw5PWpSqFzq6BSYiUsIC3zZ3abrCP6hoyc%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%7D; SKpbjs-id5id_last=Thu%2C%2007%20Jan%202021%2013%3A11%3A58%20GMT; cto_bundle=_5hjX19BYjVqRlVKRDcwRVlISWQyOENOM1I4diUyQmNxYUklMkJXRnNYNFF2RXhWbkJXcERWVXBadUN2QWJDNyUyQk9oYW0zejF1amZ6S2RqeWlWSHNzdXo1aUYlMkIlMkY3YkxEWXZPS1pkdG8lMkZrWG8lMkJFVEhOZ0lHWWVvMjJwN2hsNXd0NDdvM3hROXFwR0ZrJTJGbyUyRk5ScU1GMUc1RHZ1TWVoQ2clM0QlM0Q"
server = AternosAPI(HEADER_TOKEN, TOKEN)


class aternos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="server_start", brief="Start the aternos server")
    async def server_start(self, ctx):
        if server.GetStatus() == "Offline":
            server.StartServer()
            await ctx.send("The server is starting...")
        else:
            await ctx.send("The server is already online!")

    @commands.command(name="server_stop", brief="Stop the aternos server")
    async def server_stop(self, ctx):
        if ctx.guild.get_role(796735962402521139) in ctx.author.roles:
            if server.GetStatus() == "Starting ..." or server.GetStatus() == "Online":
                server.StopServer()
                await ctx.send("The server is stopping..")
            else:
                await ctx.send("The server is already off")
        else:
            await ctx.send("You are not allowed to use this command")

    @commands.command(name="server_status", brief="Get the server status")
    async def server_status(self, ctx):
        await ctx.send(f"The server is {server.GetStatus().lower()}")

def setup(client):
    client.add_cog(aternos(client))